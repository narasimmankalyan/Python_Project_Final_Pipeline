import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_HOST = os.getenv("MONGODB_HOST")
MONGO_PORT = os.getenv("MONGODB_PORT")
MONGO_DB = os.getenv("MONGODB_DBNAME")
MONGO_USER = os.getenv("MONGODB_USERNAME")
MONGO_PASS = os.getenv("MONGODB_PASSWORD")

# MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}"

MONGO_URL = "mongodb://admin:testtesttest@localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)
db = client["studentdb"]
collection = db["students"]
