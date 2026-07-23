from fastapi import FastAPI
from app.routers import teacher,student,course,student_course,semester,attendances,user

app = FastAPI(title="Universite Yonetim Sistemi")

app.include_router(teacher.router)
app.include_router(student.router)
app.include_router(course.router)
app.include_router(student_course.router)
app.include_router(semester.router)
app.include_router(attendances.router)
app.include_router(user.router)

