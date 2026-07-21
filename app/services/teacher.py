from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate,TeacherResponse
from app.models.course import Course


def get_teacher(db:Session,title:str|None=None,department:str|None=None,name:str|None=None):
    db_teacher=db.query(Teacher)
    if name:
        db_teacher=db_teacher.filter(Teacher.name.ilike(f"%{name}%"))                                   
    if title:#Filter birebir eşleşme kontrolü
        db_teacher=db_teacher.filter(Teacher.title==title)
    if department:#Filter birebir eşleşme kontrolü
        db_teacher=db_teacher.filter(Teacher.department==department)           
    return db_teacher.all()

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
    check_have_course=db.query(Course).filter(Course.teacher_id==teacher_id).first()
    if check_have_course:
        raise HTTPException(status_code=400,detail="Seçtiğiniz hocanın üstünde ders olduğu için silinemedi")
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