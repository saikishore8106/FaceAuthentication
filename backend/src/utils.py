import cv2
import os
from datetime import datetime

def capture_image(save_folder="captured_images"):

    # Ensure save_folder is string
    save_folder = str(save_folder)
    os.makedirs(save_folder, exist_ok=True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return None, "Cannot open camera"

    ret, frame = cap.read()
    cap.release()

    if not ret:
        return None, "Failed to capture image"
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"image_{timestamp}.jpg"
    
    # Ensure filename is string
    filename = str(filename)

    save_path = os.path.join(save_folder, filename)
    cv2.imwrite(save_path, frame)

    return save_path, None

