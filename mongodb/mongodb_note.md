connect to mongodb database:

$ docker pull rtsp/mongosh
$ docker run --rm -it rtsp/mongosh bash

# this command run in container
3aa99735e267:~# mongosh "mongodb://root:123456@192.168.56.88:27017"


# python code 
# Connect to MongoDB
import pymongo

# connect mongodb with python
client = pymongo.MongoClient("mongodb://root:123456@192.168.56.88:27017")
# Access the database
db = client["bni_database"]
# Access the collection
collection = db["items"]