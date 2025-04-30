from fastapi import HTTPException
from src.repositories.student_repository import (
    create_student,
   
)
from src.models.student_model import StudentCreate, StudentUpdate, Student

async def create_student_service(data: StudentCreate):
    try:
        student = await create_student(data)
        return student
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create student: {str(e)}")