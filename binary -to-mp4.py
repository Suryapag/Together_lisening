import pymongo
import gridfs
import os
from flask import Flask, Response

app = Flask(__name__)

# MongoDB connection configuration
username = os.getenv("MONGO_USERNAME", "suryapa9092")
password = os.getenv("MONGO_PASSWORD", "9iMXKRF89jT4vE9G")
cluster = "test0.7df1d.mongodb.net"
MONGO_URI = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Test0"

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI) 
db = client["moto"]
fs = gridfs.GridFS(db)

# Retrieve the MP4 file from GridFS
filename = "video_stearming"  #The filename stored in GridFS

@app.route('/stream')
def stream_video():
    # Retrieve the file from GridFS
    file = fs.find_one({"filename": filename})
    
    if not file:
        return "Video not found!", 404

    def generate():
        chunk_size = 1024 * 1024  # 1 MB chunks
        while chunk := file.read(chunk_size):
            yield chunk

    return Response(
        generate(),
        content_type="video/mp4",
        headers={"Content-Disposition": f"inline; filename={filename}"}
    )

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True, host='127.0.0.1', port=5000)