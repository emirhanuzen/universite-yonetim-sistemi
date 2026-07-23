from sqlalchemy import Column, Integer, String,ForeignKey,Date,Boolean
from app.db.database import Base
from sqlalchemy.orm import relationship


class Attendance(Base):
    __tablename__="attendances"
    id=Column(Integer,primary_key=True,index=True)
    student_course_id=Column(Integer,ForeignKey("student_courses.id"),nullable=False)
    date=Column(Date,nullable=False)
    is_present=Column(Boolean,nullable=False)
    
    student_course=relationship("StudentCourse",back_populates="attendances")
    