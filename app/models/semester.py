from sqlalchemy import Column, Integer, String,ForeignKey,Date
from app.db.database import Base
from sqlalchemy.orm import relationship

from app.models.course import Course

class Semester(Base):
    __tablename__="semesters"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    start_date=Column(Date,nullable=False)
    courses=relationship("Course",back_populates="semester")