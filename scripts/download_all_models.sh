export OPTION=-b
cd ../
cd action_recognition/mars; python3 mars.py ${OPTION}
cd ../../action_recognition/action_clip; python3 action_clip.py ${OPTION}
cd ../../action_recognition/st_gcn; python3 st_gcn.py ${OPTION}
cd ../../action_recognition/ax_action_recognition; python3 ax_action_recognition.py ${OPTION}
cd ../../action_recognition/va-cnn; python3 va-cnn.py ${OPTION}
cd ../../action_recognition/driver-action-recognition-adas; python3 driver-action-recognition-adas.py ${OPTION}
cd ../../anomaly_detection/padim; python3 padim.py ${OPTION}
cd ../../anomaly_detection/spade-pytorch; python3 spade-pytorch.py ${OPTION}
cd ../../anomaly_detection/patchcore; python3 patchcore.py ${OPTION}
cd ../../anomaly_detection/mahalanobisad; python3 mahalanobisad.py ${OPTION}
cd ../../audio_language_model/qwen_audio; python3 qwen_audio.py ${OPTION}
cd ../../audio_processing/crnn_audio_classification; python3 crnn_audio_classification.py ${OPTION}
cd ../../audio_processing/deepspeech2; python3 deepspeech2.py ${OPTION}
cd ../../audio_processing/pytorch-dc-tts/; python3 pytorch-dc-tts.py ${OPTION}
cd ../../audio_processing/unet_source_separation/; python3 unet_source_separation.py ${OPTION}
cd ../../audio_processing/transformer-cnn-emotion-recognition/; python3 transformer-cnn-emotion-recognition.py ${OPTION}
cd ../../audio_processing/auto_speech/; python3 auto_speech.py ${OPTION}
cd ../../audio_processing/voicefilter/; python3 voicefilter.py ${OPTION}
cd ../../audio_processing/whisper/; python3 whisper.py ${OPTION}
cd ../../audio_processing/clap/; python3 clap.py ${OPTION}
cd ../../audio_processing/wespeaker/; python3 wespeaker.py ${OPTION}
cd ../../audio_processing/tacotron2/; python3 tacotron2.py ${OPTION}
cd ../../audio_processing/silero-vad/; python3 silero-vad.py ${OPTION}
cd ../../audio_processing/rvc/; python3 rvc.py ${OPTION}
cd ../../audio_processing/crepe/; python3 crepe.py ${OPTION}
cd ../../audio_processing/vall-e-x/; python3 vall-e-x.py ${OPTION}
cd ../../audio_processing/hifigan/; python3 hifigan.py ${OPTION}
cd ../../audio_processing/distil-whisper/; python3 distil-whisper.py ${OPTION}
cd ../../audio_processing/msclap/; python3 msclap.py ${OPTION}
cd ../../audio_processing/narabas/; python3 narabas.py ${OPTION}
cd ../../audio_processing/rnnoise/; python3 rnnoise.py ${OPTION}
cd ../../audio_processing/audioset_tagging_cnn/; python3 audioset_tagging_cnn.py ${OPTION}
cd ../../audio_processing/deep-music-enhancer/; python3 deep_music_enhancer.py ${OPTION}
cd ../../audio_processing/pyannote-audio/; python3 pyannote-audio.py ${OPTION}
cd ../../audio_processing/kotoba-whisper/; python3 kotoba-whisper.py ${OPTION}
cd ../../audio_processing/reazon_speech/; python3 reazon_speech.py ${OPTION}
cd ../../audio_processing/reazon_speech2/; python3 reazon_speech2.py ${OPTION}
cd ../../audio_processing/gpt-sovits/; python3 gpt-sovits.py ${OPTION}
cd ../../audio_processing/gpt-sovits-v2/; python3 gpt-sovits-v2.py ${OPTION}
cd ../../audio_processing/bert-vits2/; python3 bert-vits2.py ${OPTION}
cd ../../audio_processing/dtln/; python3 dtln.py ${OPTION}
cd ../../audio_processing/pytorch_wavenet/; python3 pytorch_wavenet.py ${OPTION}
cd ../../audio_processing/audiosep/; python3 audiosep.py ${OPTION}
cd ../../background_ramoval/deep-image-matting; python3 deep-image-matting.py ${OPTION}
cd ../../background_ramoval/u2net; python3 u2net.py ${OPTION}
cd ../../background_ramoval/u2net; python3 u2net.py -a small ${OPTION}
cd ../../background_ramoval/u2net-portrait-matting; python3 u2net-portrait-matting.py ${OPTION}
cd ../../background_ramoval/u2net-human-seg; python3 u2net-human-seg.py ${OPTION}
cd ../../background_ramoval/indexnet; python3 indexnet.py ${OPTION}
cd ../../background_ramoval/modnet; python3 modnet.py ${OPTION}
cd ../../background_ramoval/background_matting_v2; python3 background_matting_v2.py ${OPTION}
cd ../../background_ramoval/cascade_psp; python3 cascade_psp.py ${OPTION}
cd ../../background_ramoval/rembg; python3 rembg.py ${OPTION}
cd ../../background_ramoval/dis_seg; python3 dis_seg.py ${OPTION}
cd ../../background_ramoval/gfm; python3 gfm.py ${OPTION}
cd ../../crowd_counting/crowdcount-cascaded-mtl; python3 crowdcount-cascaded-mtl.py ${OPTION}
cd ../../crowd_counting/c-3-framework; python3 c-3-framework.py ${OPTION}
cd ../../diffusion/latent-diffusion-txt2img; python3 latent-diffusion-txt2img.py ${OPTION}
cd ../../diffusion/latent-diffusion-superresolution; python3 latent-diffusion-superresolution.py ${OPTION}
cd ../../diffusion/latent-diffusion-inpainting; python3 latent-diffusion-inpainting.py ${OPTION}
cd ../../diffusion/stable-diffusion-txt2img; python3 stable-diffusion-txt2img.py ${OPTION}
cd ../../diffusion/control_net python3 control_net.py ${OPTION}
cd ../../diffusion/latent-consistency-models python3 latent-consistency-models.py ${OPTION}
cd ../../diffusion/daclip-sde; python3 daclipsde.py ${OPTION}
cd ../../diffusion/riffusion; python3 riffusion.py ${OPTION}
cd ../../diffusion/marigold; python3 marigold.py ${OPTION}
cd ../../diffusion/sdxl-turbo; python3 sdxl-turbo.py ${OPTION}
cd ../../diffusion/sd-turbo; python3 sd-turbo.py ${OPTION}
cd ../../diffusion/anything_v3; python3 anything_v3.py ${OPTION}
cd ../../diffusion/depth_anything_controlnet; python3 depth_anything_controlnet.py ${OPTION}
cd ../../deep_fashion/clothing-detection; python3 clothing-detection.py ${OPTION}
cd ../../deep_fashion/fashionai-key-points-detection; python3 fashionai-key-points-detection.py ${OPTION}
cd ../../deep_fashion/mmfashion; python3 mmfashion.py ${OPTION}
cd ../../deep_fashion/mmfashion_tryon; python3 mmfashion_tryon.py ${OPTION}
cd ../../deep_fashion/mmfashion_retrieval; python3 mmfashion_retrieval.py ${OPTION}
cd ../../deep_fashion/person-attributes-recognition-crossroad; python3 person-attributes-recognition-crossroad.py ${OPTION}
cd ../../depth_estimation/midas; python3 midas.py ${OPTION}
cd ../../depth_estimation/monodepth2; python3 monodepth2.py ${OPTION}
cd ../../depth_estimation/fcrn-depthprediction; python3 fcrn-depthprediction.py ${OPTION}
cd ../../depth_estimation/fast-depth; python3 fast-depth.py ${OPTION}
cd ../../depth_estimation/lap-depth; python3 lap-depth.py ${OPTION}
cd ../../depth_estimation/hitnet; python3 hitnet.py ${OPTION}
cd ../../depth_estimation/crestereo; python3 crestereo.py ${OPTION}
cd ../../depth_estimation/mobilestereonet; python3 mobilestereonet.py ${OPTION}
cd ../../depth_estimation/depth_anything; python3 depth_anything.py ${OPTION}
cd ../../face_detection/blazeface; python3 blazeface.py ${OPTION}
cd ../../face_detection/zoe_depth; python3 zoe_depth ${OPTION}
cd ../../face_detection/dbface; python3 dbface.py ${OPTION}
cd ../../face_detection/face-mask-detection; python3 face-mask-detection.py ${OPTION}
cd ../../face_detection/yolov1-face; python3 yolov1-face.py ${OPTION}
cd ../../face_detection/yolov3-face; python3 yolov3-face.py ${OPTION}
cd ../../face_detection/retinaface; python3 retinaface.py ${OPTION}
cd ../../face_detection/anime-face-detector; python3 anime-face-detector.py ${OPTION}
cd ../../face_detection/face-detection-adas; python3 face-detection-adas.py ${OPTION}
cd ../../face_detection/mtcnn; python3 mtcnn.py ${OPTION}
cd ../../face_identification/arcface; python3 arcface.py ${OPTION}
cd ../../face_identification/insightface; python3 insightface.py ${OPTION}
cd ../../face_identification/vggface2; python3 vggface2.py ${OPTION}
cd ../../face_identification/cosface; python3 cosface.py ${OPTION}
cd ../../face_identification/facenet_pytorch; python3 facenet_pytorch.py ${OPTION}
cd ../../face_recognition/face_alignment; python3 face_alignment.py ${OPTION}
cd ../../face_recognition/face_classification; python3 face_classification.py ${OPTION}
cd ../../face_recognition/facial_feature; python3 facial_feature.py ${OPTION}
cd ../../face_recognition/gazeml; python3 gazeml.py ${OPTION}
cd ../../face_recognition/prnet; python3 prnet.py ${OPTION}
cd ../../face_recognition/facemesh; python3 facemesh.py ${OPTION}
cd ../../face_recognition/mediapipe_iris; python3 mediapipe_iris.py ${OPTION}
cd ../../face_recognition/hopenet; python3 hopenet.py ${OPTION}
cd ../../face_recognition/ax_gaze_estimation; python3 ax_gaze_estimation.py ${OPTION}
cd ../../face_recognition/age-gender-recognition-retail; python3 age-gender-recognition-retail.py ${OPTION}
cd ../../face_recognition/ferplus; python3 ferplus.py ${OPTION}
cd ../../face_recognition/face-anti-spoofing; python3 face-anti-spoofing.py ${OPTION}
cd ../../face_recognition/ax_facial_features; python3 ax_facial_features.py ${OPTION}
cd ../../face_recognition/6d_repnet; python3 6d_repnet.py ${OPTION}
cd ../../face_recognition/hsemotion; python3 hsemotion.py ${OPTION}
cd ../../face_recognition/facemesh_v2; python3 facemesh_v2.py ${OPTION}
cd ../../face_recognition/3ddfa; python3 3ddfa$.py ${OPTION}
cd ../../face_recognition/mivolo; python3 mivolo.py ${OPTION}
cd ../../face_recognition/l2cs_net; python3 l2cs_net.py ${OPTION}
cd ../../face_recognition/gazelle; python3 gazelle.py ${OPTION}
cd ../../face_restoration/codeformer; python3 codeformer.py ${OPTION}
cd ../../face_restoration/gfpgan; python3 gfpgan.py ${OPTION}
cd ../../face_swapping/facefusion; python3 facefusion.py ${OPTION}
cd ../../face-swapping/sber-swap; python3 sber-swap.py ${OPTION}
cd ../../face-swapping/deepfacelive; python3 deepfacelive.py ${OPTION}
cd ../../frame_interpolation/flavr; python3 flavr.py ${OPTION}
cd ../../frame_interpolation/cain; python3 cain.py ${OPTION}
cd ../../frame_interpolation/film; python3 film.py ${OPTION}
cd ../../frame_interpolation/rife; python3 rife.py ${OPTION}
cd ../../generative_adversarial_networks/council-gan; python3 council-gan.py ${OPTION}
cd ../../generative_adversarial_networks/pytorch-gan; python3 pytorch-gan.py ${OPTION}
cd ../../generative_adversarial_networks/restyle-encoder; python3 restyle-encoder.py ${OPTION}
cd ../../generative_adversarial_networks/sam; python3 sam.py ${OPTION}
cd ../../generative_adversarial_networks/psgan; python3 psgan.py ${OPTION}
cd ../../generative_adversarial_networks/encoder4editing; python3 encoder4editing.py ${OPTION}
cd ../../generative_adversarial_networks/lipgan; python3 lipgan.py ${OPTION}
cd ../../generative_adversarial_networks/live_portrait; python3 live_portrait.py ${OPTION}
cd ../../hand_detection/yolov3-hand; python3 yolov3-hand.py ${OPTION}
cd ../../hand_detection/hand_detection_pytorch python3 hand_detection_pytorch.py ${OPTION}
cd ../../hand_detection/blazepalm; python3 blazepalm.py ${OPTION}
cd ../../hand_recognition/blazehand; python3 blazehand.py ${OPTION}
cd ../../hand_recognition/hand3d; python3 hand3d.py ${OPTION}
cd ../../hand_recognition/minimal-hand; python3 minimal-hand.py ${OPTION}
cd ../../hand_recognition/v2v-posenet; python3 v2v-posenet.py ${OPTION}
cd ../../hand_recognition/hands_segmentation_pytorch; python3 hands_segmentation_pytorch.py ${OPTION}
cd ../../image_captioning/illustration2vec; python3 illustration2vec.py ${OPTION}
cd ../../image_captioning/image_captioning_pytorch; python3 image_captioning_pytorch.py ${OPTION}
cd ../../image_captioning/blip2; python3 blip2.py ${OPTION}
cd ../../image_classification/efficientnet; python3 efficientnet.py ${OPTION}
cd ../../image_classification/googlenet; python3 googlenet.py ${OPTION}
cd ../../image_classification/inceptionv3; python3 inceptionv3.py ${OPTION}
cd ../../image_classification/inceptionv4; python3 inceptionv4.py ${OPTION}
cd ../../image_classification/mobilenetv2; python3 mobilenetv2.py ${OPTION}
cd ../../image_classification/mobilenetv3; python3 mobilenetv3.py ${OPTION}
cd ../../image_classification/partialconv; python3 partialconv.py ${OPTION}
cd ../../image_classification/resnet50; python3 resnet50.py ${OPTION}
cd ../../image_classification/vgg16; python3 vgg16.py ${OPTION}
cd ../../image_classification/vit; python3 vit.py ${OPTION}
cd ../../image_classification/efficientnetv2; python3 efficientnetv2.py ${OPTION}
cd ../../image_classification/wide_resnet50; python3 wide_resnet50.py ${OPTION}
cd ../../image_classification/resnet18; python3 resnet18.py ${OPTION}
cd ../../image_classification/mlp_mixer; python3 mlp_mixer.py ${OPTION}
cd ../../image_classification/alexnet; python3 alexnet.py ${OPTION}
cd ../../image_classification/clip; python3 clip.py ${OPTION}
cd ../../image_classification/japanese-clip; python3 japanese-clip.py ${OPTION}
cd ../../image_classification/japanese-stable-clip-vit-l-16; python3 japanese-stable-clip-vit-l-16.py ${OPTION}
cd ../../image_classification/clip-japanese-base; python3 clip-japanese-base.py ${OPTION}
cd ../../image_classification/weather-prediction-from-image; python3 weather-prediction-from-image.py ${OPTION}
cd ../../image_classification/convnext; python3 convnext.py ${OPTION}
cd ../../image_classification/swin-transformer; python3 swin_transformer.py ${OPTION}
cd ../../image_classification/mobileone; python3 mobileone.py ${OPTION}
cd ../../image_classification/imagenet21k; python3 imagenet21k.py ${OPTION}
cd ../../image_classification/volo; python3 volo.py ${OPTION}
cd ../../image_inpainting/3d-photo-inpainting; python3 3d-photo-inpainting.py ${OPTION}
cd ../../image_inpainting/inpainting_gmcnn; python3 inpainting_gmcnn.py ${OPTION}
cd ../../image_inpainting/pytorch-inpainting-with-partial-conv; python3 pytorch-inpainting-with-partial-conv.py ${OPTION}
cd ../../image_inpainting/deepfillv2; python3 deepfillv2.py ${OPTION}
cd ../../image_inpainting/lama; python3 lama.py ${OPTION}
cd ../../image_manipulation/dewarpnet; python3 dewarpnet.py ${OPTION}
cd ../../image_manipulation/illnet; python3 illnet.py ${OPTION}
cd ../../image_manipulation/noise2noise; python3 noise2noise.py ${OPTION}
cd ../../image_manipulation/colorization; python3 colorization.py ${OPTION}
cd ../../image_manipulation/u2net_portrait; python3 u2net_portrait.py ${OPTION}
cd ../../image_manipulation/style2paints; python3 style2paints.py ${OPTION}
cd ../../image_manipulation/deep_white_balance; python3 deep_white_balance.py ${OPTION}
cd ../../image_manipulation/deblur_gan; python3 deblur_gan.py ${OPTION}
cd ../../image_manipulation/invertible_denoising_network; python3 invertible_denoising_network.py ${OPTION}
cd ../../image_manipulation/dfm; python3 dfm.py ${OPTION}
cd ../../image_manipulation/dehamer; python3 dehamer.py ${OPTION}
cd ../../image_manipulation/dfe; python3 dfe.py ${OPTION}
cd ../../image_manipulation/pytorch-superpoint; python3 pytorch_superpoint.py ${OPTION}
cd ../../image_manipulation/cnngeometric_pytorch; python3 cnngeometric_pytorch.py ${OPTION}
cd ../../image_manipulation/lightglue; python3 lightglue.py ${OPTION}
cd ../../image_manipulation/docshadow; python3 docshadow.py ${OPTION}
cd ../../image_manipulation/fbcnn; python3 fbcnn.py ${OPTION}
cd ../../image_restoration/nafnet; python3 nafnet.py ${OPTION}
cd ../../image_segmentation/deeplabv3; python3 deeplabv3.py ${OPTION}
cd ../../image_segmentation/hair_segmentation; python3 hair_segmentation.py ${OPTION}
cd ../../image_segmentation/hrnet_segmentation; python3 hrnet_segmentation.py ${OPTION}
cd ../../image_segmentation/pspnet-hair-segmentation; python3 pspnet-hair-segmentation.py ${OPTION}
cd ../../image_segmentation/human_part_segmentation; python3 human_part_segmentation.py ${OPTION}
cd ../../image_segmentation/pytorch-unet; python3 pytorch-unet.py ${OPTION}
cd ../../image_segmentation/pytorch-enet; python3 pytorch-enet.py ${OPTION}
cd ../../image_segmentation/semantic-segmentation-mobilenet-v3; python3 semantic-segmentation-mobilenet-v3.py ${OPTION}
cd ../../image_segmentation/yet-another-anime-segmenter; python3 yet-another-anime-segmenter.py ${OPTION}
cd ../../image_segmentation/swiftnet; python3 swiftnet.py ${OPTION}
cd ../../image_segmentation/dense_prediction_transformers; python3 dense_prediction_transformers.py ${OPTION}
cd ../../image_segmentation/paddleseg; python3 paddleseg.py ${OPTION}
cd ../../image_segmentation/pp_liteseg; python3 pp_liteseg.py ${OPTION}
cd ../../image_segmentation/suim; python3 suim.py ${OPTION}
cd ../../image_segmentation/group_vit; python3 group_vit.py ${OPTION}
cd ../../image_segmentation/anime-segmentation; python3 anime-segmentation.py ${OPTION}
cd ../../image_segmentation/segment-anything; python3 segment-anything.py ${OPTION}
cd ../../image_segmentation/tusimple-DUC; python3 tusimple_DUC.py ${OPTION}
cd ../../image_segmentation/pytorch-fcn; python3 pytorch-fcn.py ${OPTION}
cd ../../image_segmentation/grounded_sam; python3 grounded_sam.py ${OPTION}
cd ../../image_segmentation/segment-anything-2; python3 segment-anything-2.py ${OPTION}
cd ../../image_segmentation/fast_sam; python3 fast_sam.py ${OPTION}
cd ../../landmark_classification/landmarks_classifier_asia; python3 landmarks_classifier_asia.py ${OPTION}
cd ../../landmark_classification/places365; python3 places365.py ${OPTION}
cd ../../line_segment_detection/mlsd; python3 mlsd.py ${OPTION}
cd ../../line_segment_detection/dexined; python3 dexined.py ${OPTION}
cd ../../low_light_image_enhancement/agllnet; python3 agllnet.py ${OPTION}
cd ../../low_light_image_enhancement/drbn_skf; python3 drbn_skf.py ${OPTION}
cd ../../natural_language_processing/bert; python3 bert.py ${OPTION}
cd ../../natural_language_processing/bert_insert_punctuation; python3 bert_insert_punctuation.py ${OPTION}
cd ../../natural_language_processing/bert_maskedlm; python3 bert_maskedlm.py ${OPTION}
cd ../../natural_language_processing/bert_ner; python3 bert_ner.py ${OPTION}
cd ../../natural_language_processing/bert_question_answering; python3 bert_question_answering.py ${OPTION}
cd ../../natural_language_processing/bert_sentiment_analysis; python3 bert_sentiment_analysis.py ${OPTION}
cd ../../natural_language_processing/bert_tweets_sentiment; python3 bert_tweets_sentiment.py ${OPTION}
cd ../../natural_language_processing/bert_zero_shot_classification; python3 bert_zero_shot_classification.py ${OPTION}
cd ../../natural_language_processing/bertjsc; python3 bertjsc.py ${OPTION}
cd ../../natural_language_processing/gpt2; python3 gpt2.py ${OPTION}
cd ../../natural_language_processing/rinna_gpt2; python3 rinna_gpt2.py ${OPTION}
cd ../../natural_language_processing/fugumt-en-ja; python3 fugumt-en-ja.py ${OPTION}
cd ../../natural_language_processing/fugumt-ja-en; python3 fugumt-en-ja.py ${OPTION}
cd ../../natural_language_processing/bert_sum_ext; python3 bert_sum_ext.py ${OPTION}
cd ../../natural_language_processing/sentence_transformers_japanese; python3 sentence_transformers_japanese.py ${OPTION}
cd ../../natural_language_processing/presumm; python3 presumm.py ${OPTION}
cd ../../natural_language_processing/t5_base_japanese_title_generation; python3 t5_base_japanese_title_generation.py ${OPTION}
cd ../../natural_language_processing/multilingual-e5; python3 multilingual-e5.py ${OPTION}
cd ../../natural_language_processing/t5_whisper_medical; python3 t5_whisper_medical.py ${OPTION}
cd ../../natural_language_processing/t5_base_japanese_summarization; python3 t5_base_japanese_summarization.py ${OPTION}
cd ../../natural_language_processing/glucose; python3 glucose.py ${OPTION}
cd ../../natural_language_processing/cross_encoder_mmarco; python3 cross_encoder_mmarco.py ${OPTION}
cd ../../natural_language_processing/soundchoice-g2p; python3 soundchoice-g2p.py ${OPTION}
cd ../../natural_language_processing/g2p_en; python3 g2p_en.py ${OPTION}
cd ../../natural_language_processing/t5_base_japanese_ner; pyhton3 t5_base_japanese_ner.py ${OPTION}
cd ../../natural_language_processing/japanese-reranker-cross-encoder; python3 japanese-reranker-cross-encoder.py ${OPTION}
cd ../../natural_language_processing/bert_ner_japanese; python3 bert_ner_japanese.py ${OPTION}
cd ../../network_intrusion_detection/bert-network-packet-flow-header-payload; python3 bert-network-packet-flow-header-payload.py ${OPTION}
cd ../../network_intrusion_detection/falcon-adapter-network-packet; python3 falcon-adapter-network-packet.py ${OPTION}
cd ../../neural_rendering/nerf; python3 nerf.py ${OPTION}
cd ../../neural_rendering/tripo_sr; python3 tripo_sr.py ${OPTION}
cd ../../object_detection/centernet; python3 centernet.py ${OPTION}
cd ../../object_detection/m2det; python3 m2det.py ${OPTION}
cd ../../object_detection/maskrcnn; python3 maskrcnn.py ${OPTION}
cd ../../object_detection/mobilenet_ssd; python3 mobilenet_ssd.py ${OPTION}
cd ../../object_detection/yolov1-tiny; python3 yolov1-tiny.py ${OPTION}
cd ../../object_detection/yolov2; python3 yolov2.py ${OPTION}
cd ../../object_detection/yolov2-tiny; python3 yolov2-tiny.py ${OPTION}
cd ../../object_detection/yolov3; python3 yolov3.py ${OPTION}
cd ../../object_detection/yolov3-tiny; python3 yolov3-tiny.py ${OPTION}
cd ../../object_detection/yolov4; python3 yolov4.py ${OPTION}
cd ../../object_detection/yolov4-tiny; python3 yolov4-tiny.py ${OPTION}
cd ../../object_detection/yolov5; python3 yolov5.py ${OPTION}
cd ../../object_detection/yolov6; python3 yolov6.py ${OPTION}
cd ../../object_detection/yolov7; python3 yolov7.py ${OPTION}
cd ../../object_detection/yolov8; python3 yolov8.py ${OPTION}
cd ../../object_detection/yolov8-seg; python3 yolov8-seg.py ${OPTION}
cd ../../object_detection/yolov9; python3 yolov9.py ${OPTION}
cd ../../object_detection/yolov10; python3 yolov10.py ${OPTION}
cd ../../object_detection/yolov11; python3 yolov11.py ${OPTION}
cd ../../object_detection/yolox; python3 yolox.py ${OPTION}
cd ../../object_detection/yolox-ti-lite; python3 yolox-ti-lite.py ${OPTION}
cd ../../object_detection/yolov; python3 yolov.py ${OPTION}
cd ../../object_detection/pedestrian_detection; python3 pedestrian_detection.py ${OPTION}
cd ../../object_detection/efficientdet; python3 efficientdet.py ${OPTION}
cd ../../object_detection/nanodet; python3 nanodet.py ${OPTION}
cd ../../object_detection/yolor; python3 yolor.py ${OPTION}
cd ../../object_detection/mobile_object_localizer; python3 mobile_object_localizer.py ${OPTION}
cd ../../object_detection/sku100k-densedet; python3 yolor.py ${OPTION}
cd ../../object_detection/traffic-sign-detection; python3 traffic-sign-detection.py ${OPTION}
cd ../../object_detection/detic; python3 detic.py ${OPTION}
cd ../../object_detection/picodet; python3 picodet.py ${OPTION}
cd ../../object_detection/yolact; python3 yolact.py ${OPTION}
cd ../../object_detection/fastest-det; python3 fastest-det.py ${OPTION}
cd ../../object_detection/dab-detr; python3 dab-detr.py ${OPTION}
cd ../../object_detection/glip; python3 glip.py ${OPTION}
cd ../../object_detection/poly_yolo; python3 poly_yolo.py ${OPTION}
cd ../../object_detection/crowd_det; python3 crowd_det.py ${OPTION}
cd ../../object_detection/footandball; python3 footandball.py ${OPTION}
cd ../../object_detection/qrcode_wechatqrode; python3 qrcode_wechatqrode.py ${OPTION}
cd ../../object_detection/layout_parsing; python3 layout_parsing.py ${OPTION}
cd ../../object_detection/damo_yolo; python3 damo_yolo.py ${OPTION}
cd ../../object_detection/groundingdino; python3 groundingdino.py ${OPTION}
cd ../../object_detection_3d/3d_bbox; python3 3d_bbox.py ${OPTION}
cd ../../object_detection_3d/3d-object-detection.pytorch; python3 3d-object-detection.pytorch.py ${OPTION}
cd ../../object_detection_3d/mediapipe_objectron; python3 mediapipe_objectron.py ${OPTION}
cd ../../object_detection_3d/egonet; python3 egonet.py ${OPTION}
cd ../../object_detection_3d/d4lcn; python3 d4lcn.py ${OPTION}
cd ../../object_detection_3d/did_m3d; python3 did_m3d.py ${OPTION}
cd ../../object_detection_3d/rt-detr-v2; python3 rt-detr-v2.py ${OPTION}
cd ../../object_tracking/centroids-reid; python3 centroids-reid.py ${OPTION}
cd ../../object_tracking/deepsort; python3 deepsort.py ${OPTION}
cd ../../object_tracking/person_reid_baseline_pytorch; python3 person_reid_baseline_pytorch.py ${OPTION}
cd ../../object_tracking/abd_net; python3 abd_net.py ${OPTION}
cd ../../object_tracking/siam-mot; python3 siam-mot.py ${OPTION}
cd ../../object_tracking/bytetrack; python3 bytetrack.py ${OPTION}
cd ../../object_tracking/qd-3dt; python3 qd-3dt.py ${OPTION}
cd ../../object_tracking/strong_sort; python3 strong_sort.py ${OPTION}
cd ../../object_tracking/deepsort_vehicle; python3 deepsort_vehicle.py ${OPTION}
cd ../../optical_flow_estimation/raft; python3 raft.py ${OPTION}
cd ../../point_segmentation/pointnet_pytorch; python3 pointnet_pytorch.py ${OPTION}
cd ../../pose_estimation/lightweight-human-pose-estimation; python3 lightweight-human-pose-estimation.py ${OPTION}
cd ../../pose_estimation/openpose; python3 openpose.py ${OPTION}
cd ../../pose_estimation/pose_resnet; python3 pose_resnet.py ${OPTION}
cd ../../pose_estimation/blazepose; python3 blazepose.py ${OPTION}
cd ../../pose_estimation/efficientpose; python3 efficientpose.py ${OPTION}
cd ../../pose_estimation/movenet; python3 movenet.py -d ${OPTION}
cd ../../pose_estimation/animalpose; python3 animalpose.py -d ${OPTION}
cd ../../pose_estimation/mediapipe_holistic; python3 mediapipe_holistic.py ${OPTION}
cd ../../pose_estimation/ap-10k; python3 ap-10k.py ${OPTION}
cd ../../pose_estimation/posenet; python3 posenet.py ${OPTION}
cd ../../pose_estimation/e2pose; python3 e2pose.py ${OPTION}
cd ../../pose_estimation_3d/3d-pose-baseline; python3 3d-pose-baseline.py ${OPTION}
cd ../../pose_estimation_3d/lightweight-human-pose-estimation-3d; python3 lightweight-human-pose-estimation-3d.py ${OPTION}
cd ../../pose_estimation_3d/blazepose-fullbody; python3 blazepose-fullbody.py ${OPTION}
cd ../../pose_estimation_3d/3dmppe_posenet; python3 3dmppe_posenet.py ${OPTION}
cd ../../pose_estimation_3d/pose-hg-3d; python3 pose-hg-3d.py ${OPTION}
cd ../../pose_estimation_3d/gast; python3 gast.py ${OPTION}
cd ../../pose_estimation_3d/mediapipe_pose_world_landmarks; python3 mediapipe_pose_world_landmarks.py ${OPTION}
cd ../../road_detection/codes-for-lane-detection; python3 codes-for-lane-detection.py ${OPTION}
cd ../../road_detection/roneld; python3 roneld.py ${OPTION}
cd ../../road_detection/road-segmentation-adas; python3 road-segmentation-adas.py ${OPTION}
cd ../../road_detection/cdnet; python3 cdnet.py ${OPTION}
cd ../../road_detection/lstr; python3 lstr.py ${OPTION}
cd ../../road_detection/ultra-fast-lane-detection; python3 ultra-fast-lane-detection.py ${OPTION}
cd ../../road_detection/yolop; python3 yolop.py ${OPTION}
cd ../../road_detection/hybridnets; python3 hybridnets.py ${OPTION}
cd ../../road_detection/polylanenet; python3 polylanenet.py ${OPTION}
cd ../../rotation_prediction/rotnet; python3 rotnet.py ${OPTION}
cd ../../nsfw_detector/clip-based-nsfw-detector; python3 clip-based-nsfw-detector.py ${OPTION}
cd ../../style_transfer/adain; python3 adain.py ${OPTION}
cd ../../style_transfer/beauty_gan; python3 beauty_gan.py ${OPTION}
cd ../../style_transfer/animeganv2; python3 animeganv2.py ${OPTION}
cd ../../style_transfer/pix2pixHD; python3 pix2pixhd.py ${OPTION}
cd ../../style_transfer/elegant; python3 elegant.py ${OPTION}
cd ../../super_resolution/srresnet; python3 srresnet.py ${OPTION}
cd ../../super_resolution/han; python3 han.py ${OPTION}
cd ../../super_resolution/edsr; python3 edsr.py ${OPTION}
cd ../../super_resolution/real-esrgan; python3 real-esrgan.py ${OPTION}
cd ../../super_resolution/rcan-it; python3 rcan-it.py ${OPTION}
cd ../../super_resolution/swinir; python3 swinir.py ${OPTION}
cd ../../super_resolution/hat; python3 hat.py ${OPTION}
cd ../../super_resolution/span; python3 span.py ${OPTION}
cd ../../text_detection/craft_pytorch; python3 craft_pytorch.py ${OPTION}
cd ../../text_detection/pixel_link; python3 pixel_link.py ${OPTION}
cd ../../text_detection/east; python3 east.py ${OPTION}
cd ../../text_recognition/etl; python3 etl.py ${OPTION}
cd ../../text_recognition/deep-text-recognition-benchmark; python3 deep-text-recognition-benchmark.py ${OPTION}
cd ../../text_recognition/crnn.pytorch; python3 crnn.pytorch.py ${OPTION}
cd ../../text_recognition/paddleocr; python3 paddleocr.py ${OPTION}
cd ../../text_recognition/easyocr; python3 easyocr.py ${OPTION}
cd ../../text_recognition/ndlocr_text_recognition; python3 ndlocr_text_recognition.py ${OPTION}
cd ../../time_series_forecasting/informer2020; python3 informer2020.py ${OPTION}
cd ../../time_series_forecasting/timesfm; python3 timesfm.py ${OPTION}
cd ../../vehicle_recognition/vehicle-attributes-recognition-barrier; python3 vehicle-attributes-recognition-barrier.py ${OPTION}
cd ../../vehicle_recognition/vehicle-license-plate-detection-barrier; python3 vehicle-license-plate-detection-barrier.py ${OPTION}
cd ../../vision_language_model/llava; python3 llava.py ${OPTION}
cd ../../vision_language_model/florence2; python3 florence2.py ${OPTION}
cd ../../vision_language_model/qwen2_vl; python3 qwen2_vl.py ${OPTION}
cd ../../vision_language_model/llava-jp; python3 llava-jp.py ${OPTION}
