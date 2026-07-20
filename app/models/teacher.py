from sqlalchemy import Column, Integer, String,ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship


class Teacher(Base):
    __tablename__ ="teachers"
    id=Column(Integer,primary_key=True, index=True)
    name=Column(String, nullable=False)
    title=Column(String)
    department=Column(String)
    courses=relationship("Course", back_populates="teacher")
