from app.models.course import Course
from app.schemas.course import  CourseResponse,CourseCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.teacher import Teacher
from app.models.student_course import StudentCourse
from app.models.semester import Semester

def get_course(db: Session,name:str|None=None,teacher_id:int|None=None,semester_id:int|None=None):
    db_course = db.query(Course)
    if name:
        db_course=db_course.filter(Course.name.ilike(f"%{name}%"))
    if teacher_id:
        db_course=db_course.filter(Course.teacher_id==teacher_id)    
    if semester_id:
        db_course=db_course.filter(Course.semester_id==semester_id)  
    return db_course.all()

def get_course_by_id(course_id: int, db: Session):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Aradığınız id'de ders yok")
    return db_course

def get_course_with_teacher(course_id:int,db:Session):
      db_course=db.query(Course).filter(Course.id==course_id).first()
      if not db_course:
            raise HTTPException(status_code=404,detail="Aradığınız id'de ders yok ")
      return db_course.teacher

def post_course(course:CourseCreate, db: Session):
    #Aynı dönem içerisinde aynı 2 ders olamaz kontrolü
    check_semester_only_course=db.query(Course).filter(Course.name==course.name,Course.semester_id==course.semester_id).first()
    if check_semester_only_course:
        raise HTTPException(status_code=400,detail="Eklemek istediğiniz ders zaten aynı dönem içinde mevcut.")
    try:    
        db_course = Course(name=course.name, teacher_id=course.teacher_id,semester_id=course.semester_id)
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
        return db_course
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=f"Kurs kayıt edilmedi:{str(e)}"
                            )

def put_course(course_id: int, course:CourseCreate, db: Session):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Aradığınız id'de ders yok")
    #Aynı dönem içerisinde aynı 2 ders olamaz kontrolü ,update de aynı kurs id'liyi pas geçer.
    check_semester_only_course=db.query(Course).filter(Course.name==course.name,Course.semester_id==course.semester_id.id,Course.id!=course_id).first()
    if check_semester_only_course:
        raise HTTPException(status_code=400,detail="Eklemek istediğiniz ders zaten aynı dönem içinde mevcut.")
    try:
        db_course.name = course.name
        db_course.teacher_id = course.teacher_id
        db_course.semester_id=course.semester_id
        db.commit()
        db.refresh(db_course)
        return db_course
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=f"Ders güncellenmedi:{str(e)}")

def delete_course(course_id: int, db: Session):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Aradığınız id'de ders yok")
    try:
        db.delete(db_course)
        db.commit()
        return f"{course_id} id'li ders silindi"
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=f"Ders silinmedi:{str(e)}")

def get_course_with_student(course_id:int,db:Session):
      db_course=db.query(Course).filter(Course.id==course_id).first()
      if not db_course:
            raise HTTPException(status_code=404,detail="Kurs bulunamadı")
      ogrenciler=[kayit.student for kayit in db_course.enrollments]
      return ogrenciler

def get_course_semester(course_id:int,db:Session):
    db_course=db.query(Course).filter(Course.id==course_id).first()
    if not db_course:
        raise HTTPException()
    return db_course.semester