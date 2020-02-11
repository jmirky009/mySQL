import pymongo
import os

MONGO_URI = ("MONGO_URI")

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = 'myTestDB'
COLLECTION_NAME = "myFirstDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is Connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)