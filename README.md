# Fullstack Project

A fullstack web application including frontend (HTML/CSS/JS), backend (FastAPI), and database (MongoDB).  
This repository is designed as a complete example for learning and building fullstack applications.

---

## 📁 Project Structure

```

demoproject/
├─ fastapi_tutorial/          # Backend (FastAPI API service)
│  └─ main.py
│
├─ html-css-js/               # Frontend (static website)
│  ├─ index.html
│  ├─ css/
│  ├─ js/
│  └─ images/
│
├─ mongodb/                   # MongoDB service (Docker Compose)
│  ├─ compose.yml
│  └─ mongodb_note.md
│
└─ README.md                  # Main documentation

````

---

## 🚀 Features

- ✔️ Frontend (HTML + CSS + JavaScript)
- ✔️ Backend API with FastAPI
- ✔️ MongoDB database (Docker)
- ✔️ Clean and modular project structure
- ✔️ Easy to start and extend

---

## 🧩 Backend Setup (FastAPI)

### Install dependencies:

```bash
cd fastapi_tutorial
pip install "fastapi[standard]"
````

### Run API server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### API documentation:

```
http://127.0.0.1:8000/docs
```

---

## 🖥️ Frontend Setup

The frontend is fully static.
Simply open:

```
html-css-js/index.html
```

Or run a simple local web server:

```bash
cd html-css-js
python3 -m http.server 9000
```

Visit:

```
http://localhost:9000
```

---

## 🗄️ Database Setup (MongoDB)

MongoDB runs via Docker Compose.

```bash
cd mongodb
docker compose up -d
```

MongoDB will be available on:

```
localhost:27017
```

---

## 🧪 Testing the API

Example:

```bash
curl http://127.0.0.1:8000/
```

Or use the built-in Swagger UI (`/docs`).

---

## 📦 Technologies Used

* FastAPI (Python)
* HTML / CSS / JavaScript
* MongoDB
* Docker / Docker Compose

---

## 📄 License

MIT License

---

## 👤 Author

Your Name
GitHub: [https://github.com/yourname](https://github.com/yourname)

---

## ⭐ If this project is helpful, please give it a star!

```


