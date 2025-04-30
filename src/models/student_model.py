from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class StudentBase(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    contact_number: str
    dob: str
    parent_name: str = Field(..., min_length=2)
    address: str = Field(None, min_length=2)
    levels: str

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    contact_number: Optional[str]
    dob: Optional[str]
    parent_name: Optional[str]
    address: Optional[str]
    levels: Optional[str]

class Student(StudentBase):
    student_id: str
