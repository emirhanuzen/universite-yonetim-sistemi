from sqlalchemy import Column, Integer, String,ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    ogrenci_no=Column(String,nullable=False,unique=True)
    registrations=relationship("StudentCourse", back_populates="student")