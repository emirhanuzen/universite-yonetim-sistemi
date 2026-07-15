from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Teacher(Base):
    __tablename__ ="teachers"
    id=Column(Integer,primary_key=True, index=True)
    name=Column(String, nullable=True)
    title=Column(String)
    department=Column(String)
    courses=relationship("Course", back_populates="teacher")

class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=True)
    registrations=relationship("StudentCourse", back_populates="student")


class Course(Base):
    __tablename__="courses"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=True)
    teacher_id=Column(Integer,ForeignKey("teachers.id"))
    teacher=relationship("Teacher", back_populates="courses")
    enrollments=relationship("StudentCourse", back_populates="course")


class StudentCourse(Base):
    __tablename__="student_courses"
    id=Column(Integer,primary_key=True,index=True)
    student_id=Column(Integer,ForeignKey("students.id"))   
    course_id=Column(Integer,ForeignKey("courses.id"))
    student=relationship("Student",back_populates="registrations")
    course=relationship("Course",back_populates="enrollments")
