from pydantic import BaseModel
from app.schemas.course import CourseResponse


class TeacherCreate(BaseModel):
    name:str
    title:str
    department:str

class TeacherResponse(BaseModel):
    id:int
    name:str | None =None
    department:str | None=None
    title:str
    class Config:
        from_attributes=True

class TeacherWithCoursesResponse(TeacherResponse):
    courses: list[CourseResponse]=[]
    class Config:
        from_attributes=True
