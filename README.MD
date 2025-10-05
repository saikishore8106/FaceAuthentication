# 🧠 Face Authentication App

A full-stack face authentication system that:
- Captures a user's face using a webcam,
- Authenticates against known images,
- Stores logs in PostgreSQL,
- Displays both captured and matched images via a React frontend.

---

## 📂 Project Structure

```bash
    project/
    ├── backend/
    │   ├── main.py           # FastAPI app
    │   ├── utils.py          # Capture image function
    │   ├── face_auth.py      # Face authentication logic
    │   ├── database.py       # PostgreSQL DB logic
    │   └── ...
    ├── frontend/
    │   ├── src/
    │   │   └── App.js        # React app
    │   └── ...
    └── data/
        ├── captured/         # Captured images
        └── images/           # Known face images

```
---

## ⚙️ Backend (FastAPI)

### 1. Install Dependencies

```bash
    cd backend
    python -m venv venv
    # Activate environment
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate

    pip install -r requirements.txt
```

### RUN BACKEND 

    uvicorn main:app --reload   


## All the endpoints
| Endpoint        | Method | Description                  |
| --------------- | ------ | ---------------------------- |
| `/`             | GET    | Health check                 |
| `/authenticate` | GET    | Capture & authenticate face  |
| `/known_faces`  | Static | Serve known reference images |

## 🗄️ Database (PostgreSQL)
### 1. Create Database & User
```sql
    CREATE DATABASE face_auth_db;
    CREATE USER your_user WITH PASSWORD 'your_password';
    GRANT ALL PRIVILEGES ON DATABASE face_auth_db TO your_user;
```

### 2. Update DB Config (database.py)
```sql
    DB_USER = "your_user"
    DB_PASSWORD = "your_password"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "face_auth_db"
```
### ⚛️ Frontend (React)
### 1. Setup

```bash
    cd frontend
    npm install
```

### 2. Run
```bash
    npm start
```


App runs at: http://localhost:3000


**NOTE**: Make sure FastAPI backend is running before launching the frontend.