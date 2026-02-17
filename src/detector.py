import logging
from ultralytics import YOLO
from .preprocess import preprocess_frame

class DefectDetector:
    def __init__(self, model_path="yolov8n.pt", confidence=0.5):
        self.model = YOLO(model_path)
        self.confidence = confidence
        logging.info(f"Loaded YOLO model from {model_path}")

    def detect(self, frame):
        processed_frame = preprocess_frame(frame)
        results = self.model(processed_frame, conf=self.confidence)
        annotated = results[0].plot()
        num_detections = len(results[0].boxes)
        return annotated, num_detections
