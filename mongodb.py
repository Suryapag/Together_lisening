import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Store your MongoDB credentials securely as environment variables
username = os.getenv("MONGO_USERNAME", "suryapa9092")
password = os.getenv("MONGO_PASSWORD", "9iMXKRF89jT4vE9G")
cluster = "test0.7df1d.mongodb.net"  # Replace with your cluster address

# Construct the URI with the credentials
uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=Test0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Connection failed: {e}")

try:
    db = client["moto"]
    colloection = db["model"]
    result = colloection.find_one()
    first_name = result.get("name")
    print(first_name)
except Exception as q:
    print(f'ERROR{q}')