from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.semester import Semester
from app.schemas.semester import SemesterCreate,SemesterResponse
from app.models.course import Course
from app.schemas.course import CourseResponse


def get_semester_all(db:Session):
    db_semester=db.query(Semester).all()
    if not db_semester:
        raise   HTTPException(status_code=404,detail="Kyıtlı dönem bulunamadı")
    return db_semester

def get_semester_by_id(semester_id:int,db:Session):
    db_semester=db.query(Semester).filter(Semester.id==semester_id).first()
    if not db_semester:
        raise HTTPException(status_code=404,detail="Aradığınız id'de  dönem bulunamadı")
    return db_semester

def get_semester_with_courses(semester_id:int,db:Session):
    db_semester=db.query(Semester).filter(Semester.id==semester_id).first()
    if not db_semester:
        raise HTTPException(status_code=404,detail="Dönem bulunamadı")    
    return db_semester.courses

def post_semester(semester:SemesterCreate,db:Session):
    db_semester=Semester(name=semester.name,start_date=semester.start_date)
    try:
        db.add(db_semester)
        db.commit()
        db.refresh(db_semester)
        return db_semester
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=f"Dönem kayıt edilmedi:{str(e)}")
 
def put_semester(semester_id:int,semester:SemesterCreate,db:Session):
    db_semester=db.query(Semester).filter(Semester.id==semester_id).first()
    if not db_semester:
        raise HTTPException(status_code=404,detail="Aradığınız dönem bulunamadı")
    db_semester.name=semester.name
    db_semester.start_date=semester.start_date
    try:
        db.commit()
        db.refresh(db_semester)
        return  db_semester 
    except Exception as e: 
        db.rollback()
        raise HTTPException(status_code=500,detail="Dönem güncellenemedi")
           

def delete_semester(semester_id:int,db:Session):
    db_semester=db.query(Semester).filter(Semester.id==semester_id).first()
    if not db_semester:
        raise HTTPException(status_code=404,detail="Aradığınız dönem bulunamadı")
    try:
        db.delete(db_semester)
        db.commit()
        return f"{semester_id}'li dönem silindi"
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=f"dönem silinemedi:{str(e)}")