import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_HOST = os.getenv("MONGODB_HOST", "localhost")
MONGO_PORT = os.getenv("MONGODB_PORT", "27017")
MONGO_DB = os.getenv("MONGODB_DBNAME", "studentdb")
MONGO_USER = os.getenv("MONGODB_USERNAME")
MONGO_PASS = os.getenv("MONGODB_PASSWORD")

if MONGO_USER and MONGO_PASS:
    MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}"
else:
    MONGO_URL = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"

print("Connecting to Mongo:", MONGO_URL)  # 🔥 debug line

client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_DB]
collection = db["students"]
