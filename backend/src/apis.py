from fastapi import FastAPI
from fastapi.responses import JSONResponse
from utils import capture_image
from face_auth import check_the_auth
from database import save_auth_log  # import database function
import os
from fastapi.staticfiles import StaticFiles

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# Allow requests from your frontend
origins = [
    "http://localhost:3000",  # React dev server
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["*"] to allow all origins (less secure)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Folder to save captured images
CAPTURED_FOLDER = r"C:\Users\saich\Downloads\YTV\Projects\data\captured"
KNOWN_FACES_FOLDER = r"C:\Users\saich\Downloads\YTV\Projects\data\known_faces"
KNOWN_FACE_NAMES = ["chandra", "Kishore"]

# Mount static folder at URL /captured
app.mount("/captured", StaticFiles(directory=CAPTURED_FOLDER), name="captured")

# Mount known images folder for browser access
app.mount("/known_faces", StaticFiles(directory=KNOWN_FACES_FOLDER), name="known_faces")


@app.get("/")
def health_check():
    return "Very good health"


@app.get("/authenticate")
async def authenticate_endpoint():
    try:
        # Capture an image
        captured_image_path, error = capture_image(save_folder=CAPTURED_FOLDER)
        if error:
            return JSONResponse(status_code=500, content={"success": False, "error": error})

        if captured_image_path is None:
            return JSONResponse(status_code=500, content={"success": False, "error": "Failed to read captured image"})

        # Run authentication
        name, e = check_the_auth(captured_image_path, KNOWN_FACES_FOLDER, KNOWN_FACE_NAMES)

        # Determine matched auth image path
        auth_image_path = None
        if name:
            index = KNOWN_FACE_NAMES.index(name)
            auth_image_file = os.listdir(KNOWN_FACES_FOLDER)[index]
            auth_image_path = os.path.join(KNOWN_FACES_FOLDER, auth_image_file)

        # Save log to database
        save_auth_log(person_name=name, captured_image_path=captured_image_path, auth_image_path=auth_image_path)

        if name:
            return {"success": True, "authenticated_as": name, "captured_image": captured_image_path, "auth_image": auth_image_path, "error": e}
        else:
            return {"success": False, "authenticated_as": None, "captured_image": captured_image_path, "message": "No match found", "error": e}

    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "error": str(e)})
