from mmdet.apis import DetInferencer

# Choose to use a config
model_name = "mmdetection/projects/CO-DETR/configs/codino/co_dino_5scale_swin_l_16xb1_16e_o365tococo.py"
# Setup a checkpoint file to load
checkpoint = "co_dino_5scale_swin_large_16e_o365tococo-614254c9.pth"

# Set the device to be used for evaluation
device = "cuda:0"

# Initialize the DetInferencer
inferencer = DetInferencer(model_name, checkpoint, device)

# Use the detector to do inference
img = "./mmdetection/demo/demo.jpg"
result = inferencer(img, out_dir="./output")
