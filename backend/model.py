import torch


class YOLOModel:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Load pre-trained YOLO model

    def predict(self, image):
        # Use the model to get predictions
        results = self.model(image)
        return results.xyxy[0].tolist()  # Return bounding box coordinates
