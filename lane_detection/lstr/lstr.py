import os, sys
import glob
import time
import numpy as np
import cv2
from tqdm import tqdm
import ailia
# import original modules
sys.path.append('../../util')
from utils import get_base_parser, update_parser, get_savepath  # noqa: E402
from model_utils import check_and_download_models  # noqa: E402
# logger
from logging import getLogger   # noqa: E402
logger = getLogger(__name__)


# ======================
# Parameters
# ======================
WEIGHT_PATH = 'lstr.onnx'
MODEL_PATH = 'lstr.onnx.prototxt'
REMOTE_PATH = 'https://storage.googleapis.com/ailia-models/lstr/'

IMAGE_PATH = 'input'
SAVE_IMAGE_PATH = 'output'

HEIGHT = 360
WIDTH = 640
VIDEO_HEIGHT = 1280
VIDEO_WIDTH = 720

DB_MEAN = [0.40789655, 0.44719303, 0.47026116]
DB_STD = [0.2886383, 0.27408165, 0.27809834]


# ======================
# Arguemnt Parser Config
# ======================
parser = get_base_parser(
    'LSTR', IMAGE_PATH, SAVE_IMAGE_PATH,
)
parser.add_argument(
    '--input_type', choices=['image', 'video'], required=True
)
parser.add_argument(
    '--input_name', required=True
)
args = update_parser(parser)


# ======================
# Main functions
# ======================
def _normalize(image, mean, std):
    image -= mean
    image /= std


def _softmax(x, axis=None):
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    e_x = e_x / np.sum(e_x, axis=axis, keepdims=True)
    return e_x


def get_files(dirname):
    files = glob.glob(dirname)
    if len(files)==0:
        print('specified files is empty.')
        exit()
    return files


def predict(net, image):
    height, width = image.shape[0:2]
    images = np.zeros((1, 3, HEIGHT, WIDTH), dtype=np.float32)
    masks = np.ones((1, 1, HEIGHT, WIDTH), dtype=np.float32)
    pad_image = image.copy()
    pad_mask = np.zeros((height, width, 1), dtype=np.float32)
    resized_image = cv2.resize(pad_image, (WIDTH, HEIGHT))
    resized_mask = cv2.resize(pad_mask, (WIDTH, HEIGHT))
    masks[0][0] = resized_mask.squeeze()
    resized_image = resized_image / 255.
    _normalize(resized_image, DB_MEAN, DB_STD)
    resized_image = resized_image.transpose(2, 0, 1)
    images[0] = resized_image
    outputs = net.predict([images, masks])
    return outputs


def postprocess(out_pred_logits, out_pred_curves, orig_target_sizes):
    out_logits = np.expand_dims(out_pred_logits[0], axis=0)
    out_curves = np.expand_dims(out_pred_curves[0], axis=0)

    assert len(out_logits) == len(orig_target_sizes)
    assert orig_target_sizes.shape[1] == 2

    prob = _softmax(out_logits, -1)
    labels = np.argmax(prob, axis=-1)
    labels[labels != 1] = 0
    labels = np.expand_dims(labels, axis=-1).astype(float)

    results = np.concatenate((labels, out_curves), axis=-1)
    return results


def draw_annotation(pred, img):
    img = (img - np.min(img)) / (np.max(img) - np.min(img))
    img = (img * 255).astype(np.uint8)
    img_h, img_w, _ = img.shape

    # Draw predictions
    # pred = pred[pred[:, 0] != 0]  # filter invalid lanes
    pred = pred[pred[:, 0].astype(int) == 1]
    overlay = img.copy()
    cv2.rectangle(img, (5, 10), (5 + 1270, 25 + 30 * pred.shape[0] + 10), (255, 255, 255), thickness=-1)
    cv2.putText(img, 'Predicted curve parameters:', (10, 30), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1.5, color=(0, 0, 0), thickness=2)

    for i, lane in enumerate(pred):
        color = (0, 255, 0)
        lane = lane[1:]  # remove conf
        lower, upper = lane[0], lane[1]
        lane = lane[2:]  # remove upper, lower positions

        # generate points from the polynomial
        ys = np.linspace(lower, upper, num=100)
        points = np.zeros((len(ys), 2), dtype=np.int32)
        points[:, 1] = (ys * img_h).astype(int)
        points[:, 0] = ((lane[0] / (ys - lane[1]) ** 2 + lane[2] / (ys - lane[1]) + lane[3] + lane[4] * ys - lane[5]) * img_w).astype(int)
        points = points[(points[:, 0] > 0) & (points[:, 0] < img_w)]

        # draw lane with a polyline on the overlay
        for current_point, next_point in zip(points[:-1], points[1:]):
            overlay = cv2.line(overlay, tuple(current_point), tuple(next_point), color=color, thickness=7)

        # draw lane ID
        if len(points) > 0:
            cv2.putText(img, str(i), tuple(points[len(points)//3]), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(0, 255, 255), thickness=5)
            content = "{}: k''={:.3}, f''={:.3}, m''={:.3}, n'={:.3}, b''={:.3}, b'''={:.3}, alpha={}, beta={}".format(
                str(i), lane[0], lane[1], lane[2], lane[3], lane[4], lane[5], int(lower * img_h),
                int(upper * img_w)
            )
            cv2.putText(img, content, (10, 30 * (i + 2)), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1.5, color=color, thickness=2)

    w = 0.5
    img = ((1. - w) * img + w * overlay).astype(np.uint8) # Add lanes overlay
    return img


def main():
    # model files check and download
    check_and_download_models(WEIGHT_PATH, MODEL_PATH, REMOTE_PATH)

    print('ftype={}, input_type={}, input_name={}'.format(args.ftype, args.input_type, args.input_name))

    net = ailia.Net(MODEL_PATH, WEIGHT_PATH, env_id=args.env_id)
    orig_target_sizes = np.expand_dims(np.array([HEIGHT, WIDTH]), axis=0)

    if not os.path.exists('./output'):
        os.mkdir('./output')
    if not os.path.exists('./output/image'):
        os.mkdir('./output/image')
    if not os.path.exists('./output/video'):
        os.mkdir('./output/video')

    if args.ftype == 'image':
        # image to image
        if args.input_type == 'image':
            image_file = get_files('./input/image/{}'.format(args.input_name))
            image = cv2.imread('{}'.format(image_file[0]))
            out_pred_logits, out_pred_curves, _, _, weights = predict(net, image)
            results = postprocess(out_pred_logits, out_pred_curves, orig_target_sizes)
            preds = draw_annotation(results[0], image)
            cv2.imwrite('./output/image/{}'.format(os.path.basename(image_file[-1]) + '.jpg'), preds)

        # video to image
        elif args.input_type == 'video':
            print('Not implemented.')
            exit()

    elif args.ftype == 'video':
        # image to video
        if args.input_type == 'image':
            print('Not implemented.')
            exit()

        # video to video
        elif args.input_type == 'video':
            cap = cv2.VideoCapture('./input/video/{}'.format(args.input_name))
            if not cap.isOpened():
                print('Video is not opened.')
                exit()
            filename = '_'.join(args.input_name.split('/'))

            output_video = cv2.VideoWriter(
                    './output/video/{}'.format(filename),
                    cv2.VideoWriter_fourcc('m','p','4', 'v'), #mp4フォーマット
                    float(30), #fps
                    (VIDEO_HEIGHT, VIDEO_WIDTH) #size
            )

            i = 1
            pbar = tqdm(total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
            while True:
                pbar.update(i)
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv2.resize(frame, dsize=(VIDEO_HEIGHT, VIDEO_WIDTH))
                out_pred_logits, out_pred_curves, _, _, weights = predict(net, frame)
                results = postprocess(out_pred_logits, out_pred_curves, orig_target_sizes)
                preds = draw_annotation(results[0], frame)
                output_video.write(preds)
            cap.release()
            output_video.release()
        print('Video saved as {}'.format(filename))

    else:
        print('invalid ftype.')
        exit()


if __name__ == '__main__':
    main()
