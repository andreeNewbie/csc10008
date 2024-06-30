import os
import pymongo


# check if connect to database or not
try:
    myClient = pymongo.MongoClient(os.getenv("MONGODB_URL"))
    db = myClient["send_file_project"]
    user_col = db["users"]
    print("Connected to MongoDB successfully!")
except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
