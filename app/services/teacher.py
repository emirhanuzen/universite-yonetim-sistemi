from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate,TeacherResponse


def get_all_teacher(db:Session):
        db_teacher=db.query(Teacher).all()       
        return db_teacher

def get_teacher_by_id(teacher_id:int,db:Session):
      db_teacher=db.query(Teacher).filter(Teacher.id==teacher_id).first()
      if not db_teacher:
        raise HTTPException(status_code=404,detail=f"{teacher_id}'idli öğretmen bulunamadı")       
      return db_teacher

def post_teacher(teacher:TeacherCreate,db:Session):   
    try:
        db_teacher=Teacher(name=teacher.name,title=teacher.title,department=teacher.department)      
        db.add(db_teacher)
        db.commit()
        db.refresh(db_teacher)
        return db_teacher 
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=f"Hoca oluşturalamadı:{str(e)}")
         
def put_teacher(teacher_id:int,teacher:TeacherCreate,db:Session):
    db_teacher=db.query(Teacher).filter(Teacher.id==teacher_id).first()  
    if not db_teacher:
        raise HTTPException(status_code=404,detail="Hoca bulunamadı") 
    try:         
        db_teacher.name=teacher.name
        db_teacher.title=teacher.title
        db_teacher.department=teacher.department
        db.commit()
        db.refresh(db_teacher)
        return db_teacher
    except Exception as e:
         db.rollback()
         raise HTTPException(status_code=500,detail="Öğretmen güncellenmedi")

def delete_teacher(teacher_id:int,db:Session):
    db_teacher=db.query(Teacher).filter(Teacher.id==teacher_id).first()
    if not db_teacher:
        raise HTTPException(status_code=404,detail="Hoca bulunamadı") 
    try:           
        db.delete(db_teacher)
        db.commit()
        return f"{teacher_id} id'li hoca silindi"
    except Exception as e:
         db.rollback()
         raise HTTPException(status_code=500,detail=f"Hoca silinemedi:{str(e)}")


def get_teacher_with_course(teacher_id:int,db:Session):
      db_teacher=db.query(Teacher).filter(Teacher.id==teacher_id).first()
      if not db_teacher:
           raise HTTPException(status_code=404,detail="Aradağınız hoca bulunamadı")
      return db_teacher