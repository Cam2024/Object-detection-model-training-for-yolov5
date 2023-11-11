# Object-detection-model-training-for-yolov5

The model uses a YOLO v5s model, deployed on a Jetson Xavier NX, which balances speed and accuracy. The model was trained using part of the publicly available dataset versus part of the dataset collected via ROS. Model deployment used the ROS system with the Triton inference server. The final result is a smart cart that can detect both carts and people.

Customized datasets of people and cars:
<img width="1609" alt="人的数据集" src="https://github.com/Cam2024/Object-detection-model-training-for-yolov5/assets/89662823/4f504762-a946-4e07-bc14-f57dc91daec2">

An Example of Object Detection:

<img width="325" alt="屏幕截图 2023-08-01 154157" src="https://github.com/Cam2024/Object-detection-model-training-for-yolov5/assets/89662823/83b7b189-723b-4787-8350-1154467a5c1f">
