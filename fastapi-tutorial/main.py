from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pymongo
from bson import ObjectId
from datetime import datetime
from kafka_producer import send_task_event

app = FastAPI()

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://root:123456@192.168.88.88:27017")


# Access the database
db = client["task_database"]

# # Access the collection
# collection = db["items"]

# Allow CORS for the frontend server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for Task
class Tasks(BaseModel):
    taskName: str
    taskDescription: str
    taskStatus: str
    taskDueDate: str


# Helper function to convert MongoDB documents to JSON-compatible dicts
# documents = list(collection.find())
# [{'_id': ObjectId('6699ffe79ba89c0e5c1b8866'), 'carName': 'BMW 3'}] ===> [{'_id': '6699ffe79ba89c0e5c1b8866', 'carName': 'BMW 3'}]
def convert_to_json_compatible(documents: list[dict]) -> list[dict]:
    for doc in documents:
        if '_id' in doc and isinstance(doc['_id'], ObjectId):
            doc['_id'] = str(doc['_id'])
    return documents


@app.get("/tasks/")
async def get_tasks():
    # Access the collection
    collection = db["tasks"]
    # Find all documents in the collection
    tasks = list(collection.find())
    convert_to_json_compatible(tasks)
    # tasks = list(collection.find({}, {'_id': 0}))
    # return {"tasks": str(tasks)}
    return tasks


# @app.post("/tasks/")
# async def add_task(task: Tasks):
#     # Insert the item into the database

#     # Access the collection
#     collection = db["tasks"]
#     # Insert the document into the collection
#     try:
#         result = collection.insert_one(task.model_dump())
#         print(f"Document inserted with _id: {result.inserted_id}")
#         return {"success": True, "message": f"Document inserted with _id: {result.inserted_id}"}
#     except Exception as e:
#         print("An error occurred while inserting the document:", e)
#         return {"success": False, "message": "An error occurred while inserting the document."}
@app.post("/tasks/")
async def add_task(task: Tasks):
    collection = db["tasks"]

    try:
        result = collection.insert_one(task.model_dump())

        event = {
            "eventType": "TASK_CREATED",
            "taskId": str(result.inserted_id),
            "taskName": task.taskName,
            "taskDescription": task.taskDescription,
            "taskStatus": task.taskStatus,
            "taskDueDate": task.taskDueDate,
            "timestamp": datetime.now().isoformat()
        }

        send_task_event(event)

        return {
            "success": True,
            "message": f"Document inserted with _id: {result.inserted_id}"
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "message": str(e)
        }


@app.put("/tasks/{task_id}")
async def update_task(task_id: str, updated_task: Tasks):
    collection = db["tasks"]

    try:
        old_task = collection.find_one({"_id": ObjectId(task_id)})

        if not old_task:
            raise HTTPException(
                status_code=404,
                detail=f"Task with ID {task_id} not found"
            )

        update_data = updated_task.model_dump()

        result = collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": update_data}
        )

        event = {
            "eventType": "TASK_UPDATED",
            "taskId": task_id,
            "oldTask": {
                "taskName": old_task.get("taskName"),
                "taskDescription": old_task.get("taskDescription"),
                "taskStatus": old_task.get("taskStatus"),
                "taskDueDate": old_task.get("taskDueDate")
            },
            "newTask": update_data,
            "timestamp": datetime.now().isoformat()
        }

        send_task_event(event)

        return {
            "success": True,
            "message": f"Task {task_id} updated successfully",
            "updatedFields": update_data
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    collection = db["tasks"]

    try:
        task = collection.find_one({"_id": ObjectId(task_id)})

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        result = collection.delete_one({"_id": ObjectId(task_id)})

        event = {
            "eventType": "TASK_DELETED",
            "taskId": task_id,
            "taskName": task.get("taskName"),
            "taskDescription": task.get("taskDescription"),
            "taskStatus": task.get("taskStatus"),
            "taskDueDate": task.get("taskDueDate"),
            "timestamp": datetime.now().isoformat()
        }

        send_task_event(event)

        return {
            "success": True,
            "message": f"Document deleted with _id: {task_id}"
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "message": str(e)
        }



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
