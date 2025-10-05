import os
import cv2
import numpy as np
from face_compare import face_authentication
import face_recognition

def check_the_auth(captured_image, folder_path, known_face_names):
    """
    Compare a captured image against images in a folder and return the matched name and any error.
    
    captured_image: Image to check (numpy array or compatible format)
    folder_path: Path containing known images
    known_face_names: List of names corresponding to known images
    """
    name = None  # Default if no matc
    error = None  # Store any exception

    known_encodings = []

    print(folder_path, len( os.listdir(folder_path)))
    
    unknown_image = face_recognition.load_image_file(captured_image)
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    try:
        # Loop over all images in folder
        for image_from_db in os.listdir(folder_path):
            print("PART 2")
            file_path = os.path.join(folder_path, image_from_db)
            print(file_path)
            known_image = face_recognition.load_image_file(file_path)
            known_encoding = face_recognition.face_encodings(known_image)[0]
            known_encodings.append(known_encoding)

        matches, face_distances = face_authentication(known_encodings, unknown_encoding)
        print(matches, face_distances)
        best_match_index = np.argmin(face_distances)

        # TODO: DO IT FOR MULTIPLE CANDIDATES
        if matches[best_match_index]:
            name = known_face_names[best_match_index]


    except Exception as e:
        print(f"Error checking authentication: {e}")
        error = e

    return name, error