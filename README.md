# 🚀 Fullstack Task Tracker (FastAPI + MongoDB + Kafka)

A fullstack web application demonstrating a simple **event-driven architecture** using FastAPI, MongoDB, and Apache Kafka.

---

## 📌 Project Overview

This project is designed for learning and practicing:

- Fullstack development
- Event-driven architecture
- Kafka integration

---

## 🧠 Architecture

Frontend (HTML/JS)
        ↓
FastAPI (CRUD API)
        ↓
MongoDB (Data storage)
        ↓
Kafka Producer (Send events)
        ↓
Kafka Topic (task-events)
        ↓
Kafka Consumer (Process events)

---

## 📁 Project Structure

```
fullstack-project/
├─ fastapi-tutorial/
│  ├─ main.py
│  ├─ kafka_producer.py
│  ├─ kafka_consumer.py
│
├─ html-css-js/
│  ├─ index.html
│  ├─ css/
│  ├─ js/
│  └─ images/
│
├─ kafka/
│  └─ compose.yml
│
├─ mongodb/
│  └─ compose.yml
│
└─ README.md
```

---

## 🚀 Features

- ✔️ Task CRUD system
- ✔️ MongoDB persistence
- ✔️ Kafka event streaming
- ✔️ Decoupled architecture
- ✔️ Real-time event logging (via consumer)

---

## 🧩 Backend Setup

```bash
cd fastapi-tutorial
pip install fastapi uvicorn pymongo kafka-python
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

## 🗄️ MongoDB Setup

```bash
cd mongodb
docker compose up -d
```

---

## 🧵 Kafka Setup

```bash
cd kafka
docker compose up -d
```

Kafka UI:

```
http://<your-ip>:8090
```

---

## ⚡ Kafka Usage

### Topic

```
task-events
```

### Event Example

```json
{
  "eventType": "TASK_CREATED",
  "taskId": "xxx",
  "taskName": "install docker",
  "taskStatus": "Pending",
  "timestamp": "2026-04-25T10:00:00"
}
```

### Event Types

- TASK_CREATED
- TASK_UPDATED
- TASK_DELETED

---

## 🧪 Run Kafka Consumer

```bash
cd fastapi-tutorial
python kafka_consumer.py
```

Output:

```
Received task event: {...}
```

---

## 🔥 Key Kafka Concepts

- Producer → Sends events
- Topic → Event stream
- Consumer → Processes events
- Decoupling → Independent systems

---

## 📈 Future Improvements

- Multi-consumer architecture
- Kafka partitions
- Real-time dashboard
- AI / analytics integration
- IoT data streaming

---

## 👨‍💻 Author

Shibu  
GitHub: https://github.com/luogeshibu

---

## ⭐ Star this repo if helpful!
