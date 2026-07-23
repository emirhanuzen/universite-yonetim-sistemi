from sqlalchemy import Column, Integer, String,ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True)
    hashed_password=Column(String,nullable=False)
    role=Column(String,nullable=False,default="user")
