from typing import Optional
from fastapi import HTTPException, status
from pydantic import BaseModel, EmailStr, validator
from datetime import date, datetime


class UserCreateIN(BaseModel):
    name: str
    email: str
    dob: Optional[str] = None
    contact_number: str
    user_type: int
    register_number: Optional[int] = None


class AddSubject(BaseModel):
    subject_name: str


class AddMark(BaseModel):
    user_id: int
    semester: int
    subject_id: int
    grade: str
