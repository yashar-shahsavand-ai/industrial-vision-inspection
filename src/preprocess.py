import cv2

def preprocess_frame(frame, width=640, height=480):
    """
    Resize and normalize frame for YOLO detection
    """
    resized = cv2.resize(frame, (width, height))
    return resized
