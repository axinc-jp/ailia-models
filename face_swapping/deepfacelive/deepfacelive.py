import sys
import time
from dataclasses import dataclass
from enum import IntEnum

# logger
from logging import getLogger  # noqa

import numpy as np
import cv2
from PIL import Image

import ailia

# import original modules
sys.path.append("../../util")
from arg_utils import get_base_parser, update_parser, get_savepath  # noqa
from model_utils import check_and_download_models  # noqa
from detector_utils import load_image  # noqa
from nms_utils import nms_boxes  # noqa
from webcamera_utils import get_capture, get_writer  # noqa

from util_math import *

logger = getLogger(__name__)


# ======================
# Parameters
# ======================

WEIGHT_G_PATH = ".onnx"
MODEL_G_PATH = ".onnx.prototxt"
REMOTE_PATH = "https://storage.googleapis.com/ailia-models/deepfacelive/"

IMAGE_PATH = "Obama.jpg"
SOURCE_PATH = "Kim Chen Yin.jpg"
SAVE_IMAGE_PATH = "output.png"


# ======================
# Arguemnt Parser Config
# ======================

parser = get_base_parser("DeepFaceLive", IMAGE_PATH, SAVE_IMAGE_PATH)
parser.add_argument("-src", "--source", default=SOURCE_PATH, help="source image")
parser.add_argument(
    "--use_sr", action="store_true", help="True for super resolution on swap image"
)
parser.add_argument("--onnx", action="store_true", help="execute onnxruntime version.")
args = update_parser(parser)


# ======================
# Class Definitions
# ======================


class ELandmarks2D(IntEnum):
    L5 = 0
    L68 = 1
    L106 = 2
    L468 = 3


@dataclass
class FLandmarks2D:
    """
    Describes 2D face landmarks in uniform float coordinates
    """

    type: ELandmarks2D = None
    ulmrks: np.ndarray = None


class AlignMode(IntEnum):
    FROM_RECT = 0
    FROM_POINTS = 1
    FROM_STATIC_RECT = 2


@dataclass
class FaceSwapInfo:
    image_name: str = None
    face_urect: np.ndarray = None
    face_pose: np.ndarray = None
    face_ulmrks: FLandmarks2D = None

    face_resolution: int = None
    face_align_image_name: str = None
    face_align_mask_name: str = None
    face_align_lmrks_mask_name: str = None
    face_anim_image_name: str = None
    face_swap_image_name: str = None
    face_swap_mask_name: str = None

    image_to_align_uni_mat = None
    face_align_ulmrks: FLandmarks2D = None


# ======================
# Secondaty Functions
# ======================


def setup_yolov5face(net):
    def fit_in(
        img,
        TW=None,
        TH=None,
        pad_to_target: bool = False,
        allow_upscale: bool = False,
        interpolation: "ImageProcessor.Interpolation" = None,
    ) -> float:
        """
        fit image in w,h keeping aspect ratio

            TW,TH           int/None     target width,height

            pad_to_target   bool    pad remain area with zeros

            allow_upscale   bool    if image smaller than TW,TH it will be upscaled

            interpolation   ImageProcessor.Interpolation. value

        returns scale float value
        """
        img = img[None, ...]
        N, H, W, C = img.shape

        if TW is not None and TH is None:
            scale = TW / W
        elif TW is None and TH is not None:
            scale = TH / H
        elif TW is not None and TH is not None:
            SW = W / TW
            SH = H / TH
            scale = 1.0
            if SW > 1.0 or SH > 1.0 or (SW < 1.0 and SH < 1.0):
                scale /= max(SW, SH)
        else:
            raise ValueError("TW or TH should be specified")

        if not allow_upscale and scale > 1.0:
            scale = 1.0

        if scale != 1.0:
            img = img.transpose((1, 2, 0, 3)).reshape((H, W, N * C))
            img = cv2.resize(
                img,
                (int(W * scale), int(H * scale)),
                interpolation=cv2.INTER_LINEAR,
            )
            H, W = img.shape[0:2]
            img = img.reshape((H, W, N, C)).transpose((2, 0, 1, 3))

        if pad_to_target:
            w_pad = (TW - W) if TW is not None else 0
            h_pad = (TH - H) if TH is not None else 0
            if w_pad != 0 or h_pad != 0:
                img = np.pad(img, ((0, 0), (0, h_pad), (0, w_pad), (0, 0)))

        return img, scale

    def pad_to_next_divisor(img, dw=None, dh=None) -> "ImageProcessor":
        """
        pad image to next divisor of width/height

         dw,dh  int
        """
        _, H, W, _ = img.shape

        w_pad = 0
        if dw is not None:
            w_pad = W % dw
            if w_pad != 0:
                w_pad = dw - w_pad

        h_pad = 0
        if dh is not None:
            h_pad = H % dh
            if h_pad != 0:
                h_pad = dh - h_pad

        if w_pad != 0 or h_pad != 0:
            img = np.pad(img, ((0, 0), (0, h_pad), (0, w_pad), (0, 0)))

        return img

    def np_sigmoid(x: np.ndarray):
        """
        sigmoid with safe check of overflow
        """
        x = -x
        c = x > np.log(np.finfo(x.dtype).max)
        x[c] = 0.0
        result = 1 / (1 + np.exp(x))
        result[c] = 0.0
        return result

    def process_pred(pred, img_w, img_h, anchor):
        pred_h = pred.shape[-3]
        pred_w = pred.shape[-2]
        anchor = np.float32(anchor)[None, :, None, None, :]

        (
            _xv,
            _yv,
        ) = np.meshgrid(
            np.arange(pred_w),
            np.arange(pred_h),
        )
        grid = (
            np.stack((_xv, _yv), 2)
            .reshape((1, 1, pred_h, pred_w, 2))
            .astype(np.float32)
        )

        stride = (img_w // pred_w, img_h // pred_h)

        pred[..., [0, 1, 2, 3, 4]] = np_sigmoid(pred[..., [0, 1, 2, 3, 4]])

        pred[..., 0:2] = (pred[..., 0:2] * 2 - 0.5 + grid) * stride
        pred[..., 2:4] = (pred[..., 2:4] * 2) ** 2 * anchor
        return pred

    def predict(img):
        N, C, H, W = img.shape

        # feedforward
        if not args.onnx:
            output = net.predict([img])
        else:
            output = net.run(None, {"in": img})

        # YoloV5Face returns 3x [N,C*16,H,W].
        # C = [cx,cy,w,h,thres, 5*x,y of landmarks, cls_id ]
        # Transpose and cut first 5 channels.
        pred0, pred1, pred2 = [
            pred.reshape((N, C, 16, pred.shape[-2], pred.shape[-1])).transpose(
                0, 1, 3, 4, 2
            )[..., 0:5]
            for pred in output
        ]

        pred0 = process_pred(pred0, W, H, anchor=[[4, 5], [8, 10], [13, 16]]).reshape(
            (1, -1, 5)
        )
        pred1 = process_pred(
            pred1, W, H, anchor=[[23, 29], [43, 55], [73, 105]]
        ).reshape((1, -1, 5))
        pred2 = process_pred(
            pred2, W, H, anchor=[[146, 217], [231, 300], [335, 433]]
        ).reshape((1, -1, 5))

        preds = np.concatenate([pred0, pred1, pred2], 1)[..., :5]
        return preds

    def extract(
        img,
        threshold: float = 0.3,
        fixed_window=0,
        min_face_size=8,
        augment=False,
    ):
        """
        arguments
            img    np.ndarray      ndim 2,3,4

            fixed_window(0)    int  size
                        0 mean don't use
                        fit image in fixed window
                        downscale if bigger than window
                        pad if smaller than window
                        increases performance, but decreases accuracy

            min_face_size(8)

            augment(False)     bool    augment image to increase accuracy
                                    decreases performance

        returns a list of [l,t,r,b] for every batch dimension of img
        """
        H, W, _ = img.shape
        if H > 2048 or W > 2048:
            fixed_window = 2048

        if fixed_window != 0:
            fixed_window = max(32, max(1, fixed_window // 32) * 32)
            img, img_scale = fit_in(
                img, fixed_window, fixed_window, pad_to_target=True, allow_upscale=False
            )
        else:
            img = pad_to_next_divisor(img, 64, 64)
            img_scale = 1.0

        _, H, W, _ = img.shape
        img = img.astype(np.float32) / 255.0

        in_img = img.transpose(0, 3, 1, 2)
        preds = predict(in_img)

        if augment:
            in_img = img[:, :, ::-1, :].transpose(0, 3, 1, 2)
            rl_preds = predict(in_img)
            rl_preds[:, :, 0] = W - rl_preds[:, :, 0]
            preds = np.concatenate([preds, rl_preds], 1)

        faces_per_batch = []
        for pred in preds:
            pred = pred[pred[..., 4] >= threshold]

            x, y, w, h, score = pred.T

            l, t, r, b = x - w / 2, y - h / 2, x + w / 2, y + h / 2
            boxes = np.stack((l, t, r, b), axis=1)
            keep = nms_boxes(boxes, score, 0.5)
            l, t, r, b = l[keep], t[keep], r[keep], b[keep]

            faces = []
            for l, t, r, b in np.stack([l, t, r, b], -1):
                if img_scale != 1.0:
                    l, t, r, b = (
                        l / img_scale,
                        t / img_scale,
                        r / img_scale,
                        b / img_scale,
                    )

                if min(r - l, b - t) < min_face_size:
                    continue
                faces.append((l, t, r, b))

            faces_per_batch.append(faces)

        return faces_per_batch

    return extract


def as_4pts(pts, w_h=None) -> np.ndarray:
    """
    get rect as 4 pts

        0--3
        |  |
        1--2

        w_h(None)    provide (w,h) to scale uniform rect to target size

    returns np.ndarray (4,2) 4 pts with w,h
    """
    if w_h is not None:
        return pts * w_h
    return pts.copy()


def face_ulmrks_transform(face_ulmrks, mat, invert=False) -> "FLandmarks2D":
    """
    Tranforms FLandmarks2D using affine mat and returns new FLandmarks2D()

     mat : np.ndarray
    """
    if invert:
        mat = cv2.invertAffineTransform(mat)

    ulmrks = face_ulmrks.ulmrks.copy()
    ulmrks = np.expand_dims(ulmrks, axis=1)
    ulmrks = cv2.transform(ulmrks, mat, ulmrks.shape).squeeze()

    return FLandmarks2D(type=face_ulmrks.type, ulmrks=ulmrks)


# ======================
# Main functions
# ======================


def face_detector(models, tar_img):
    H, W, _ = tar_img.shape

    detector_threshold = 0.5
    fixed_window_size = 480

    face_detector = models["face_detector"]
    rects = face_detector(
        tar_img,
        threshold=detector_threshold,
        fixed_window=fixed_window_size,
    )
    rects = rects[0]

    # to list of FaceURect
    rects = [
        np.array([[l, t], [l, b], [r, b], [r, t]], np.float32)
        for l, t, r, b in [[l / W, t / H, r / W, b / H] for l, t, r, b in rects]
    ]

    # rects = sort_by_area_size(rects)

    info = []

    max_faces = 1
    temporal_smoothing = 1
    if len(rects) != 0:
        max_faces = max_faces
        if max_faces != 0 and len(rects) > max_faces:
            rects = rects[:max_faces]

        # if temporal_smoothing != 1:
        #     if len(self.temporal_rects) != len(rects):
        #         self.temporal_rects = [[] for _ in range(len(rects))]

        for face_id, face_urect in enumerate(rects):
            # if temporal_smoothing != 1:
            #     if not is_frame_reemitted or len(self.temporal_rects[face_id]) == 0:
            #         self.temporal_rects[face_id].append(face_urect.as_4pts())

            #     self.temporal_rects[face_id] = self.temporal_rects[face_id][
            #         -temporal_smoothing:
            #     ]

            #     face_urect = FRect.from_4pts(np.mean(self.temporal_rects[face_id], 0))

            if polygon_area(face_urect) != 0:
                info.append(FaceSwapInfo(face_urect=face_urect))

        return info


def face_urect_cut(fsi, frame_image, coverage, resolution):
    pass


def face_urect_cut(
    fsi,
    img: np.ndarray,
    coverage: float,
    output_size: int,
    x_offset: float = 0,
    y_offset: float = 0,
):
    """
    Cut the face to square of output_size from img with given coverage using this rect

    returns image,
            uni_mat     uniform matrix to transform uniform img space to uniform cutted space
    """

    # Face rect is not a square, also rect can be rotated

    h, w = img.shape[0:2]

    # Get scaled rect pts to target img
    pts = fsi.as_4pts(w_h=(w, h))

    # Estimate transform from global space to local aligned space with bounds [0..1]
    mat = Affine2DMat.umeyama(pts, uni_rect, True)

    # get corner points in global space
    g_p = mat.invert().transform_points([(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)])
    g_c = g_p[4]

    h_vec = (g_p[1] - g_p[0]).astype(np.float32)
    v_vec = (g_p[3] - g_p[0]).astype(np.float32)

    # calc diagonal vectors between corners in global space
    tb_diag_vec = segment_to_vector(g_p[0], g_p[2]).astype(np.float32)
    bt_diag_vec = segment_to_vector(g_p[3], g_p[1]).astype(np.float32)

    mod = segment_length(g_p[0], g_p[4]) * coverage

    g_c += h_vec * x_offset + v_vec * y_offset

    l_t = np.array(
        [g_c - tb_diag_vec * mod, g_c + bt_diag_vec * mod, g_c + tb_diag_vec * mod],
        np.float32,
    )

    mat = Affine2DMat.from_3_pairs(
        l_t, np.float32(((0, 0), (output_size, 0), (output_size, output_size)))
    )
    uni_mat = Affine2DUniMat.from_3_pairs(
        (l_t / (w, h)).astype(np.float32), np.float32(((0, 0), (1, 0), (1, 1)))
    )

    face_image = cv2.warpAffine(img, mat, (output_size, output_size), cv2.INTER_CUBIC)
    return face_image, uni_mat


def get_convexhull_mask(
    face_align_ulmrks, h_w, color=(1,), dtype=np.float32
) -> np.ndarray:
    """ """
    h, w = h_w
    ch = len(color)
    lmrks = (face_align_ulmrks.ulmrks * h_w).astype(np.int32)
    mask = np.zeros((h, w, ch), dtype=dtype)
    cv2.fillConvexPoly(mask, cv2.convexHull(lmrks), color)
    return mask


def opencv_lbf(face_image):
    pass


def google_facemesh(face_image):
    pass


def insightface_2d106(face_image):
    pass


def from_3D_468_landmarks(lmrks):
    """ """
    mat = np.empty((3, 3))
    mat[0, :] = (lmrks[454] - lmrks[234]) / np.linalg.norm(lmrks[454] - lmrks[234])
    mat[1, :] = (lmrks[152] - lmrks[6]) / np.linalg.norm(lmrks[152] - lmrks[6])
    mat[2, :] = np.cross(mat[0, :], mat[1, :])
    pitch, yaw, roll = rotation_matrix_to_euler(mat)

    face_rect = np.array([pitch, yaw * 2, roll], np.float32)
    return face_rect


def face_marker(models, frame_image, fsi_list, marker_coverage=1.4):
    is_opencv_lbf = False
    is_google_facemesh = True
    is_insightface_2d106 = False
    temporal_smoothing = 1

    # if temporal_smoothing != 1 and \
    #     len(self.temporal_lmrks) != len(fsi_list):
    #     self.temporal_lmrks = [ [] for _ in range(len(fsi_list)) ]

    for face_id, fsi in enumerate(fsi_list):
        if fsi.face_urect is not None:
            # Cut the face to feed to the face marker
            face_image, face_uni_mat = face_urect_cut(
                fsi,
                frame_image,
                marker_coverage,
                (
                    256
                    if is_opencv_lbf
                    else (
                        192
                        if is_google_facemesh
                        else 192 if is_insightface_2d106 else 0
                    )
                ),
            )
            # _,H,W,_ = ImageProcessor(face_image).get_dims()
            H = W = 192
            if is_opencv_lbf:
                lmrks = opencv_lbf(face_image)[0]
            elif is_google_facemesh:
                lmrks = google_facemesh(face_image)[0]
            elif is_insightface_2d106:
                lmrks = insightface_2d106(face_image)[0]

            if temporal_smoothing != 1:
                if not is_frame_reemitted or len(self.temporal_lmrks[face_id]) == 0:
                    self.temporal_lmrks[face_id].append(lmrks)
                self.temporal_lmrks[face_id] = self.temporal_lmrks[face_id][
                    -temporal_smoothing:
                ]
                lmrks = np.mean(self.temporal_lmrks[face_id], 0)

            if is_google_facemesh:
                fsi.face_pose = from_3D_468_landmarks(lmrks)

            if is_opencv_lbf:
                lmrks /= (W, H)
            elif is_google_facemesh:
                lmrks = lmrks[..., 0:2] / (W, H)
            elif is_insightface_2d106:
                lmrks = lmrks[..., 0:2] / (W, H)

            face_ulmrks = FLandmarks2D(
                type=(
                    ELandmarks2D.L68
                    if is_opencv_lbf
                    else (
                        ELandmarks2D.L468
                        if is_google_facemesh
                        else ELandmarks2D.L106 if is_insightface_2d106 else None
                    )
                ),
                ulmrks=lmrks,
            )
            face_ulmrks = face_ulmrks_transform(face_ulmrks, face_uni_mat, invert=True)
            fsi.face_ulmrks = face_ulmrks

    return fsi_list


def face_aligner(models, frame_image, fsi_list, face_coverage=2.2, resolution=256):
    head_mode = False
    freeze_z_rotation = False
    align_mode = AlignMode.FROM_RECT
    x_offset = y_offset = 0.0

    for face_id, fsi in enumerate(fsi_list):
        head_yaw = None
        if head_mode or freeze_z_rotation:
            if fsi.face_pose is not None:
                head_yaw = fsi.face_pose.as_radians()[1]

        face_ulmrks = fsi.face_ulmrks
        if face_ulmrks is not None:
            fsi.face_resolution = resolution

            H, W = frame_image.shape[:2]
            if align_mode == AlignMode.FROM_RECT:
                face_align_img, uni_mat = face_urect_cut(
                    fsi,
                    frame_image,
                    coverage=face_coverage,
                    output_size=resolution,
                    x_offset=x_offset,
                    y_offset=y_offset,
                )
            # elif align_mode == AlignMode.FROM_POINTS:
            #     face_align_img, uni_mat = face_ulmrks.cut(
            #         frame_image,
            #         state.face_coverage + (1.0 if head_mode else 0.0),
            #         state.resolution,
            #         exclude_moving_parts=state.exclude_moving_parts,
            #         head_yaw=head_yaw,
            #         x_offset=state.x_offset,
            #         y_offset=state.y_offset - 0.08 + (-0.50 if head_mode else 0.0),
            #         freeze_z_rotation=freeze_z_rotation,
            #     )
            # elif align_mode == AlignMode.FROM_STATIC_RECT:
            #     rect = FRect.from_ltrb(
            #         [
            #             0.5 - (fsi.face_resolution / W) / 2,
            #             0.5 - (fsi.face_resolution / H) / 2,
            #             0.5 + (fsi.face_resolution / W) / 2,
            #             0.5 + (fsi.face_resolution / H) / 2,
            #         ]
            #     )
            #     face_align_img, uni_mat = rect.cut(
            #         frame_image,
            #         coverage=state.face_coverage,
            #         output_size=state.resolution,
            #         x_offset=state.x_offset,
            #         y_offset=state.y_offset,
            #     )

            # fsi.face_align_image_name = f"{frame_image_name}_{face_id}_aligned"
            fsi.image_to_align_uni_mat = uni_mat
            fsi.face_align_ulmrks = face_ulmrks_transform(uni_mat)
            fsi.face_align_image_name = face_align_img

            # Due to FaceAligner is not well loaded, we can make lmrks mask here
            face_align_lmrks_mask_img = get_convexhull_mask(
                fsi.face_align_ulmrks,
                face_align_img.shape[:2],
                color=(255,),
                dtype=np.uint8,
            )
            # fsi.face_align_lmrks_mask_name = (
            #     f"{frame_image_name}_{face_id}_aligned_lmrks_mask"
            # )
            fsi.face_align_lmrks_mask_name = face_align_lmrks_mask_img

    return fsi_list


def face_animator(models, frame_image, fsi_list):
    animator_face_id = 0
    relative_power = 0.72

    for i, fsi in enumerate(fsi_list):
        if animator_face_id == i:
            face_align_image = fsi.face_align_image_name
            if face_align_image is not None:
                # _, H, W, _ = ImageProcessor(face_align_image).get_dims()

                # if self.driving_ref_motion is None:
                #     self.driving_ref_motion = lia_model.extract_motion(face_align_image)

                anim_image = generate(
                    animatable_img,
                    face_align_image,
                    driving_ref_motion,
                    power=state.relative_power,
                )
                anim_image = ImageProcessor(anim_image).resize((W, H)).get_image("HWC")

                # fsi.face_swap_image_name = f"{fsi.face_align_image_name}_swapped"
                fsi.face_swap_image_name = anim_image
            break


def generate(
    img_source: np.ndarray,
    img_driver: np.ndarray,
    driver_start_motion: np.ndarray,
    power,
):
    """

    arguments

        img_source             np.ndarray      HW HWC 1HWC   uint8/float32

        img_driver             np.ndarray      HW HWC 1HWC   uint8/float32

        driver_start_motion    reference motion for driver
    """
    ip = ImageProcessor(img_source)
    dtype = ip.get_dtype()
    _, H, W, _ = ip.get_dims()

    out = self._generator.run(
        ["out"],
        {
            "in_src": ip.resize(self.get_input_size())
            .ch(3)
            .swap_ch()
            .to_ufloat32(as_tanh=True)
            .get_image("NCHW"),
            "in_drv": ImageProcessor(img_driver)
            .resize(self.get_input_size())
            .ch(3)
            .swap_ch()
            .to_ufloat32(as_tanh=True)
            .get_image("NCHW"),
            "in_drv_start_motion": driver_start_motion,
            "in_power": np.array([power], np.float32),
        },
    )[0].transpose(0, 2, 3, 1)[0]

    out = (
        ImageProcessor(out)
        .to_dtype(dtype, from_tanh=True)
        .resize((W, H))
        .swap_ch()
        .get_image("HWC")
    )
    return out


def deepfacelive(models, tar_img):
    tar_img = cv2.imread("Obama.jpg")

    fsi_list = face_detector(models, tar_img)
    if len(fsi_list) == 0:
        return None

    fsi_list = face_marker(models, tar_img, fsi_list)
    fsi_list = face_aligner(models, tar_img, fsi_list)
    fsi_list = face_animator(models, tar_img, fsi_list)

    aligned_face_id = 0
    for i, fsi in enumerate(fsi_list):
        if aligned_face_id == i:
            aligned_face = fsi.face_align_image_name
            break

    for fsi in fsi_list:
        swapped_face = fsi.face_swap_image_name
        if swapped_face is not None:
            break

    return aligned_face, swapped_face


def recognize_from_image(models):
    source_path = args.source
    logger.info("Source: {}".format(source_path))

    # input image loop
    for image_path in args.input:
        logger.info("Target: {}".format(image_path))

        # prepare input data
        tar_img = load_image(image_path)
        tar_img = cv2.cvtColor(tar_img, cv2.COLOR_BGRA2BGR)

        # inference
        logger.info("Start inference...")
        if args.benchmark:
            logger.info("BENCHMARK mode")
            total_time_estimation = 0
            for i in range(args.benchmark_count):
                start = int(round(time.time() * 1000))
                output = deepfacelive(models, tar_img)
                end = int(round(time.time() * 1000))
                estimation_time = end - start

                # Loggin
                logger.info(f"\tailia processing estimation time {estimation_time} ms")
                if i != 0:
                    total_time_estimation = total_time_estimation + estimation_time

            logger.info(
                f"\taverage time estimation {total_time_estimation / (args.benchmark_count - 1)} ms"
            )
        else:
            output = deepfacelive(models, tar_img)

        aligned_face, swapped_face = output
        if aligned_face is not None and swapped_face is not None:
            view_image = np.concatenate((aligned_face, swapped_face), 1)

            # plot result
            savepath = get_savepath(args.savepath, image_path, ext=".png")
            logger.info(f"saved at : {savepath}")
            cv2.imwrite(savepath, view_image)

    logger.info("Script finished successfully.")


def recognize_from_video(models):
    video_file = args.video if args.video else args.input[0]
    capture = get_capture(video_file)
    assert capture.isOpened(), "Cannot capture source"

    source_path = args.source
    logger.info("Source: {}".format(source_path))

    # create video writer if savepath is specified as video format
    if args.savepath != SAVE_IMAGE_PATH:
        f_h = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        f_w = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        writer = get_writer(args.savepath, f_h, f_w)
    else:
        writer = None

    frame_shown = False
    while True:
        ret, frame = capture.read()
        if (cv2.waitKey(1) & 0xFF == ord("q")) or not ret:
            break
        if frame_shown and cv2.getWindowProperty("frame", cv2.WND_PROP_VISIBLE) == 0:
            break

        # inference
        output = predict(models, frame)

        if args.use_sr:
            output = face_enhancement(net_pix2pix, output)

        if output:
            # plot result
            res_img = get_final_img(output, frame, net_lmk)
        else:
            res_img = frame

        # show
        cv2.imshow("frame", res_img)
        frame_shown = True

        # save results
        if writer is not None:
            writer.write(res_img)

    capture.release()
    cv2.destroyAllWindows()
    if writer is not None:
        writer.release()

    logger.info("Script finished successfully.")


def main():
    # # model files check and download
    # check_and_download_models(WEIGHT_G_PATH, MODEL_G_PATH, REMOTE_PATH)

    env_id = args.env_id

    # initialize
    if not args.onnx:
        # net_iface = ailia.Net(MODEL_ARCFACE_PATH, WEIGHT_ARCFACE_PATH, env_id=env_id)
        pass
    else:
        import onnxruntime

        net_face = onnxruntime.InferenceSession("YoloV5Face.onnx")

    extract = setup_yolov5face(net_face)

    models = {"face_detector": extract}

    if args.video is not None:
        recognize_from_video(models)
    else:
        recognize_from_image(models)


if __name__ == "__main__":
    main()
