import enum
from sqlalchemy import Column, Integer, String,ForeignKey,Enum as SqlEnum
from app.db.database import Base
from sqlalchemy.orm import relationship

class UserRole(str,enum.Enum):
    ADMIN="admin"
    USER="user"
    STUDENT="student"
    TEACHER="teacher"    

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True)
    hashed_password=Column(String,nullable=False)
    role=Column(SqlEnum(UserRole),nullable=False,default="user")
