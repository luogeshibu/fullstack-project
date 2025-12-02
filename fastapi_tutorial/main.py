from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pymongo
from bson import ObjectId

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


@app.post("/tasks/")
async def add_task(task: Tasks):
    # Insert the item into the database

    # Access the collection
    collection = db["tasks"]
    # Insert the document into the collection
    try:
        result = collection.insert_one(task.model_dump())
        print(f"Document inserted with _id: {result.inserted_id}")
        return {"success": True, "message": f"Document inserted with _id: {result.inserted_id}"}
    except Exception as e:
        print("An error occurred while inserting the document:", e)
        return {"success": False, "message": "An error occurred while inserting the document."}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    # Access the collection
    collection = db["tasks"]
    # Delete the document from the collection
    try:
        result = collection.delete_one({"_id": ObjectId(task_id)})
        print(f"Document deleted with _id: {task_id}")
        return {"success": True, "message": f"Document deleted with _id: {task_id}"}
    except Exception as e:
        print("An error occurred while deleting the document:", e)
        return {"success": False, "message": "An error occurred while deleting the document."}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
