"""
Real-Time Defect Detection System
---------------------------------
Author: Yashar Shahsavand
Description:
This project demonstrates a real-time industrial inspection
system using YOLOv8 for defect detection via webcam.
"""

import cv2
import argparse
import logging
from src.detector import DefectDetector

def parse_arguments():
    parser = argparse.ArgumentParser(description="Real-Time Defect Detection System")
    parser.add_argument("--model", type=str, default="yolov8n.pt",
                        help="Path to YOLO model")
    parser.add_argument("--confidence", type=float, default=0.5,
                        help="Confidence threshold")
    parser.add_argument("--camera", type=int, default=0,
                        help="Camera index")
    return parser.parse_args()

def initialize_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def main():
    args = parse_arguments()
    initialize_logger()

    logging.info("Initializing defect detector...")
    detector = DefectDetector(model_path=args.model, confidence=args.confidence)

    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        logging.error("Failed to open camera.")
        return

    logging.info("System started. Press 'Q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            logging.warning("Failed to grab frame.")
            break

        annotated_frame, num_detections = detector.detect(frame)

        if num_detections > 0:
            status = f"DEFECT DETECTED ({num_detections}) - FAIL"
            color = (0, 0, 255)
        else:
            status = "NO DEFECT - PASS"
            color = (0, 200, 0)

        cv2.putText(
            annotated_frame,
            status,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2
        )

        cv2.imshow("Industrial Inspection System", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    logging.info("System shutdown successfully.")

if __name__ == "__main__":
    main()
