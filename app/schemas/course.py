from pydantic import BaseModel

class CourseCreate(BaseModel):
    name:str
    teacher_id:int

class CourseResponse(BaseModel):
    id:int
    name:str
    teacher_id:int
    class Config:
        from_attributes=True