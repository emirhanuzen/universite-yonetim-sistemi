from pydantic import BaseModel
class StudentCourseCreate(BaseModel):
    student_id:int
    course_id:int
    midterm_grade:int | None=None
    final_grade:int | None=None

class StudentCourseResponse(BaseModel):
    id:int
    student_id:int
    course_id:int
    midterm_grade:int | None=None
    final_grade:int | None=None   
    class Config:
        from_attributes=True   