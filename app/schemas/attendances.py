from pydantic import BaseModel
from datetime import date

class CreateAttendances(BaseModel):
    student_course_id:int
    date:str
    is_present:bool=True   

class AttendancesResponse(BaseModel):
    id:int
    student_course_id:int
    date:date
    is_present:bool=True
    class Config:
        from_attributes=True