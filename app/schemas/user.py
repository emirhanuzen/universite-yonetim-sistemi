from pydantic import BaseModel,Field
from app.schemas.course import CourseResponse
from typing import Literal

class UserCreate(BaseModel):
    username:str =Field(min_length=3,max_length=30)
    password:str =Field(min_length=6,max_length=12)
   

class UserResponse(BaseModel):
    id:int
    username:str
    role:Literal["admin","user","student","teacher"]
    class Config:
        from_attributes:True
