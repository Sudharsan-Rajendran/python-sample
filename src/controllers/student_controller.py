from fastapi import APIRouter
from src.services.student_service import (
    create_student_service,
   
)
from src.models.student_model import Student, StudentCreate, StudentUpdate

router = APIRouter()

@router.post("/", response_model=Student)
async def create_student(data: StudentCreate):
    return await create_student_service(data)