from motor.motor_asyncio import AsyncIOMotorClient
from utils.db import database
from src.models.student_model import Student, StudentCreate, StudentUpdate
from bson import ObjectId
from typing import List, Optional

COLLECTION_NAME = "student"

async def create_student(data: StudentCreate) -> Student:
    collection = database[COLLECTION_NAME]
    student_data = data.dict()
    student_data["_id"] = str(ObjectId())  # MongoDB automatically generates an _id field
    result = await collection.insert_one(student_data)
    student_data["student_id"] = str(result.inserted_id)
    return Student(**student_data)