from pydantic import BaseModel

class StudentResponse(BaseModel):
    id:int
    name:str
    ogrenci_no:str
    class Config:
        from_attributes=True

class StudentCreate(BaseModel):
    name:str 
    ogrenci_no:str        



