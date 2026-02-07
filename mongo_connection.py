import os
from pymongo import MongoClient

client = MongoClient(os.getenv('MONGO_URI'))
db = client[os.getenv('MONGO_DB_NAME')]
coll = db[os.getenv('MONGO_COLLECTION')]
print("MongoDB connection established successfully!")