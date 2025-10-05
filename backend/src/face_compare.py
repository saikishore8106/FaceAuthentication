import face_recognition


def face_authentication(known_face_encodings, unknown_encoding):

    results = face_recognition.compare_faces(known_face_encodings, unknown_encoding)

    # Or instead, use the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, unknown_encoding)


    return results, face_distances