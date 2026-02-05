import cv2
import os
from datetime import datetime

def capture_image(save_folder="captured_images"):

    # Ensure save_folder is string
    save_folder = str(save_folder)
    os.makedirs(save_folder, exist_ok=True)

    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    if not cap.isOpened():
        return None, "Cannot open camera"
    
    for _ in range(20):
        cap.read()

    ret, frame = cap.read()
    print(ret)

    if not ret:
        return None, "Failed to capture image"
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"image_{timestamp}.jpg"
    
    # Ensure filename is string
    filename = str(filename)

    save_path = os.path.join(save_folder, filename)
    print(frame)
    cv2.imwrite(save_path, frame)
    cap.release()

    return save_path, None

