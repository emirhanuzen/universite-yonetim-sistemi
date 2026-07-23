from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class StudentCourse(Base):
    __tablename__="student_courses"
    id=Column(Integer,primary_key=True,index=True)
    student_id=Column(Integer,ForeignKey("students.id"))   
    course_id=Column(Integer,ForeignKey("courses.id"))
    midterm_grade=Column(Integer,nullable=True)
    final_grade=Column(Integer,nullable=True)
    student=relationship("Student",back_populates="registrations")
    course=relationship("Course",back_populates="enrollments")
    attendances=relationship("Attendance",back_populates="student_course")
