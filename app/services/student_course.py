from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.student_course import StudentCourse
from app.schemas.student_course import StudentCourseCreate,StudentCourseResponse
from app.schemas.student import StudentCreate,StudentResponse
from app.models.course import Course
from app.models.student import Student

def get_student_course(db:Session,student_id:int|None=None,course_id:int|None=None):
      db_student_course=db.query(StudentCourse)
      if not db_student_course:
            raise HTTPException(status_code=404,detail="Kayıtlı ders eşleşmeleri bulunamadı")
      if student_id:
            db_student_course=db_student_course.filter(StudentCourse.student_id==student_id)
      if course_id:
            db_student_course=db_student_course.filter(StudentCourse.course_id==course_id)
      return db_student_course.all()


def get_student_course_by_id(studentCourse_id:int,db:Session):   
      student_course=db.query(StudentCourse).filter(StudentCourse.id==studentCourse_id).first()
      if not student_course:
            raise HTTPException(status_code=404,detail="Kayıtlı ders eşleşmesi bulunamadı ")
      return student_course

def post_student_course(studentCourse:StudentCourseCreate,db:Session):
      student_id_check=db.query(Student).filter(Student.id==studentCourse.student_id).first()     
      if not student_id_check:
            raise Exception(status_code=404,detail="Kayıtlı öğrenci id bulunamadı")
      course_id_check=db.query(Course).filter(Course.id==studentCourse.course_id).first()
      if not course_id_check:
            raise HTTPException(status_code=404,detail="Kayıtlı ders id bulunamadı")                 
      try:
            db_student_course=StudentCourse(student_id=studentCourse.student_id,course_id=studentCourse.course_id,
         midterm_grade=studentCourse.midterm_grade,final_grade=studentCourse.final_grade)
            db.add(db_student_course)
            db.commit()
            db.refresh(db_student_course)
            return db_student_course
      except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500,detail=f"Ders öğrenciye atanamadı:{str(e)}")

def delete_student_course(student_course_id:int,db:Session):
      db_student_course=db.query(StudentCourse).filter(StudentCourse.id==student_course_id).first()
      if not db_student_course:
            raise Exception(status_code=404,detail="Eşleşme bulunamadı")
      try:
          db.delete(db_student_course)
          db.commit()
          return f"{student_course_id}'idli eşleşme silindi"
      except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500,detail=f"Öğrenci kurs eşleşmesi silinemedi:{str(e)}")

#Grade'i güncelleme sadece grade
def put_student_course(grade:StudentCourseCreate,db:Session):       
    db_student_course=db.query(StudentCourse).filter(StudentCourse.student_id==grade.student_id,
    StudentCourse.course_id==grade.course_id).first()
    if not db_student_course:
        raise Exception(status_code=404,detail="Eşleşme bulunamadı")
    try:
        db_student_course.midterm_grade=grade.midterm_grade
        db_student_course.final_grade=grade.final_grade
        db.commit()
        db.refresh(db_student_course)
        return db_student_course
    except Exception as e:
          db.rollback()
          raise HTTPException(status_code=500,detail=f"Not güncellenmedi:{str(e)}")

