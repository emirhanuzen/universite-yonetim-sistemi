from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.student import Student
from app.schemas.student import StudentCreate,StudentResponse
from app.models.student_course import StudentCourse


def get_student(db:Session,name:str|None=None,no:str|None=None):
      db_student=db.query(Student)
      if name:
           db_student=db_student.filter(Student.name.ilike(f"%{name}%"))
      if no:
           db_student=db_student.filter(Student.ogrenci_no==no)
      return db_student.all()

def get_student_by_id(student_id:int,db:Session):
      db_student=db.query(Student).filter(Student.id==student_id).first()
      if not db_student:
            raise HTTPException(status_code=404,detail="Aradığınız id'de öğrenci yok")
      return db_student            


def post_student(student:StudentCreate,db:Session):
        try:
          check_student=db.query(Student).filter(Student.ogrenci_no==student.ogrenci_no).first()
          if check_student:
               raise HTTPException(status_code=400,detail="yazdığınız öğrenci no zaten sistemde mevcut")
          db_student=Student(name=student.name,ogrenci_no=student.ogrenci_no)
          db.add(db_student)
          db.commit()
          db.refresh(db_student)
          return db_student          
        except Exception as e:
              db.rollback()
              raise HTTPException(status_code=500,detail=f"Öğrenci Oluşmadı:{str(e)}")  

def put_student(student_id:int,student:StudentCreate,db:Session):          
      db_student=db.query(Student).filter(Student.id==student_id).first()      
      if not db_student:
            raise HTTPException(status_code=404,detail="Aradığınız id'de öğrenci yok")
      check_student=db.query(Student).filter(Student.ogrenci_no==student.ogrenci_no,Student.id!=student_id).first()
      if check_student:
           raise HTTPException(status_code=400,detail="yazdığınız öğrenci no zaten sistemde mevcut")
      try:
        db_student.name=student.name
        db_student.ogrenci_no=student.ogrenci_no
        db.commit()
        db.refresh(db_student)
        return db_student
      except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=f"Öğrenci güncellenmedi{str(e)}")  

def delete_student(student_id:int,db:Session):
    db_student=db.query(Student).filter(Student.id==student_id).first()
    if not db_student:
            raise HTTPException(status_code=404,detail="Aradığınız id'de öğrenci yok")
    try:
      db.delete(db_student)
      db.commit()
      return f"{student_id}'idye sahip öğrenci silindi" 
    except Exception as e:
         db.rollback()
         raise HTTPException(status_code=500,detail=f"Öğrenci silinemedi:{str(e)}")
      
def get_with_courses(student_id:int,db:Session):
      db_student=db.query(Student).filter(Student.id==student_id).first()
      if not db_student:
            raise HTTPException(status_code=404,detail="Öğrenci bulunamadı")
      dersler=[kayit.course for kayit in db_student.registrations]
      return dersler     

