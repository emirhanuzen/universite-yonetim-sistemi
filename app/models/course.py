from sqlalchemy import Column, Integer, String,ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__="courses"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    teacher_id=Column(Integer,ForeignKey("teachers.id"),nullable=False)
    teacher=relationship("Teacher", back_populates="courses")
    enrollments=relationship("StudentCourse", back_populates="course")
    semester_id=Column(Integer,ForeignKey("semesters.id"),nullable=False)
    semester=relationship("Semester",back_populates="courses")

