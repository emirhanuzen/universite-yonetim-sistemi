from pydantic import BaseModel

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


class StudentResponse(BaseModel):
    id:int
    name:str
    ogrenci_no:str
    class Config:
        from_attributes=True

class CourseCreate(BaseModel):
    name:str
    teacher_id:int

class CourseResponse(BaseModel):
    id:int
    name:str
    teacher_id:int
    class Config:
        from_attributes=True

class TeacherWithCoursesResponse(TeacherResponse):
    courses: list[CourseResponse]=[]
    class Config:
        from_attributes=True
class StudentCreate(BaseModel):
    name:str 
    ogrenci_no:str        

class StudentCourseCreate(BaseModel):
    student_id:int
    course_id:int

class StudentCourseResponse(BaseModel):
    id:int
    student_id:int
    course_id:int
    class Config:
        from_attributes=True   