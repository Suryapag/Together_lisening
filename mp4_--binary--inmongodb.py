from bson.binary import Binary
import pymongo
import gridfs
import os

username = os.getenv("MONGO_USERNAME", "suryapa9092")
password = os.getenv("MONGO_PASSWORD", "9iMXKRF89jT4vE9G")
cluster = "test0.7df1d.mongodb.net"  # Replace with your cluster address
# MongoDB connection URI (replace with your actual connection string)
MONGO_URI = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Test0"

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client["moto"]
collection = db["model"]
fs = gridfs.GridFS(db)

# Get the path to the video file
video_path = r"D:\Movies\DC\1409899-uhd_3840_2160_25fps.mp4"

try:
    # Open the video file and store it in GridFS
    with open(video_path, "rb") as file:
        file_id = fs.put(file, filename=video_path.split("/")[-1])
        print(f"Video stored successfully with file ID: {file_id}")
except FileNotFoundError:
    print(f"File not found: {video_path}")
except Exception as e:
    print(f"An error occurred: {e}")
