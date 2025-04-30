
from motor.motor_asyncio import AsyncIOMotorClient
# from pymongo import MongoClient

MONGO_URI = "xxxxxx"  # Your MongoDB connection string
DATABASE_NAME = "python_api"  # Your MongoDB database name

client = AsyncIOMotorClient(MONGO_URI)
database = client[DATABASE_NAME]



