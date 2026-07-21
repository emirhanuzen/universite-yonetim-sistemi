from pydantic import BaseModel
from datetime import date

class SemesterCreate(BaseModel):
    name:str
    start_date:date
    
    

class SemesterResponse(BaseModel):
    id:int
    name:str
    start_date:date
    class Config:
        from_attributes=True