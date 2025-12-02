# Fullstack Project

A fullstack web application including frontend (HTML/CSS/JS), backend (FastAPI), and database (MongoDB).  
This repository is designed as a complete example for learning and building fullstack applications.

---

## 📁 Project Structure

demoproject/
├─ fastapi_tutorial/ # Backend (FastAPI API service)
│ ├─ main.py
│ 
│ 
│
├─ html-css-js/ # Frontend (static website)
│ ├─ index.html
│ ├─ css/
│ ├─ js/
│ └─ images/
│
├─ mongodb/ # MongoDB service (Docker Compose)
│ ├─ compose.yml
│ └─ mongodb_note.md
│
└─ README.md # Main documentation


---

## 🚀 Features

- ✔️ Frontend (HTML + CSS + JavaScript)
- ✔️ Backend API with FastAPI
- ✔️ MongoDB database (Docker)
- ✔️ Clean and modular project structure
- ✔️ Easy to start and extend

---

## 🖥️ Frontend Setup

The frontend is fully static.  
Simply open:


pip install "fastapi[standard]"


# run python fastapi 
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

http://127.0.0.1:8000/docs
