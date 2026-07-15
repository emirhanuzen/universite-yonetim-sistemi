from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, Base, engine
import models
import schemas

app = FastAPI(title="Universite Yonetim Sistemi")

#Base.metadata.create_all(bind=engine)  

@app.get("/teacher",response_model=list[schemas.TeacherResponse])
async def get_teacher(db:Session=Depends(get_db)):
        db_teacher=db.query(models.Teacher).all()
        if not db_teacher:
            raise HTTPException(status_code=404,detail="Hoca bulunamadı")
        return db_teacher

@app.get("/teacher_by_id/{teacher_id}",response_model=schemas.TeacherResponse)
async def get_teacher(teacher_id:int,db:Session=Depends(get_db)):
      db_teacher=db.query(models.Teacher).filter(models.Teacher.id==teacher_id).first()
      if not db_teacher:
            raise HTTPException(status_code=404,detail="Aradığınız id'de hoca yok")
      return db_teacher

@app.post("/teacher",response_model=schemas.TeacherResponse)
async def post_teacher(teacher:schemas.TeacherCreate,db:Session=Depends(get_db)):
      db_teacher=models.Teacher(name=teacher.name,title=teacher.title,department=teacher.department)
      db.add(db_teacher)
      db.commit()
      db.refresh(db_teacher)
      return db_teacher  

@app.put("/teacher/{teacher_id}",response_model=schemas.TeacherResponse)
async def put_teacher(teacher_id:int,teacher:schemas.TeacherCreate,db:Session=Depends(get_db)):
      db_teacher=db.query(models.Teacher).filter(models.Teacher.id==teacher_id).first()
      if not db_teacher:
            raise HTTPException(status_code=404,detail="Güncellemek istedğiniz hoca bulunamadı")
      db_teacher.name=teacher.name
      db_teacher.title=teacher.title
      db_teacher.department=teacher.department
      db.commit()
      db.refresh(db_teacher)
      return db_teacher

@app.delete("/teacher/{teacher_id}")
async def delete_teacher(teacher_id:int,db:Session=Depends(get_db)):
      db_teacher=db.query(models.Teacher).filter(models.Teacher.id==teacher_id).first()
      if not db_teacher:
            raise HTTPException(status_code=404,detail="Silmek  istedğiniz hoca bulunamadı")
      db.delete(db_teacher)
      db.commit()
      return f"{teacher_id} id'li hoca silindi"


#student


@app.get("/student",response_model=list[schemas.StudentResponse])
async def get_student_all(db:Session=Depends(get_db)):
      db_student=db.query(models.Student).all()
      if not db_student:
            raise HTTPException(status_code=404,detail="Öğrenci Bulunamadı")
      return db_student

@app.get("/student_by_id/{student_id}",response_model=schemas.StudentResponse)
async def get_student(student_id:int,db:Session=Depends(get_db)):
      db_student=db.query(models.Student).filter(models.Student.id==student_id).first()
      if not db_student:
            raise HTTPException(status_code=404,detail="Aradığınız id'de öğrenci yok")
      return db_student            

@app.post("/student",response_model=schemas.StudentResponse)
async def post_student(student:schemas.StudentCreate,db:Session=Depends(get_db)):
          db_student=models.Student(name=student.name,ogrenci_no=student.ogrenci_no)
          db.add(db_student)
          db.commit()
          db.refresh(db_student)
          return db_student          

@app.put("/student/{student_id}",response_model=schemas.StudentResponse)
async def put_student(student_id:int,student:schemas.StudentCreate,db:Session=Depends(get_db)):
      db_student=db.query(models.Student).filter(models.Student.id==student_id).first()
      if not db_student:
            raise HTTPException(status_code=404,detail="Aradığınız id'de öğrenci yok")
      db_student.name=student.name
      db_student.ogrenci_no=student.ogrenci_no
      db.commit()
      db.refresh(db_student)
      return db_student

@app.delete("/student/{student_id}")
async def delete_student(student_id:int,db:Session=Depends(get_db)):
      db_student=db.query(models.Student).filter(models.Student.id==student_id).first()
      if not db_student:
            raise HTTPException(status_code=404,detail="Aradığınız id'de öğrenci yok")
      db.delete(db_student)
      db.commit()
      return f"{student_id}'idye sahip öğrenci silindi" 


#course


@app.get("/course", response_model=list[schemas.CourseResponse])
async def get_course_all(db: Session = Depends(get_db)):
    db_course = db.query(models.Course).all()
    if not db_course:
        raise HTTPException(status_code=404, detail="Ders bulunamadı")
    return db_course

@app.get("/course_by_id/{course_id}", response_model=schemas.CourseResponse)
async def get_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Aradığınız id'de ders yok")
    return db_course

@app.post("/course", response_model=schemas.CourseResponse)
async def post_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = models.Course(name=course.name, teacher_id=course.teacher_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@app.put("/course/{course_id}", response_model=schemas.CourseResponse)
async def put_course(course_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Aradığınız id'de ders yok")
    db_course.name = course.name
    db_course.teacher_id = course.teacher_id
    db.commit()
    db.refresh(db_course)
    return db_course

@app.delete("/course/{course_id}")
async def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Aradığınız id'de ders yok")
    db.delete(db_course)
    db.commit()
    return f"{course_id} id'li ders silindi"


#StudentCourse

@app.get("/studentCourse",response_model=list[schemas.StudentCourseResponse])
async def get_studentCourse(db:Session=Depends(get_db)):
      db_studentCourse=db.query(models.StudentCourse).all()
      if not db_studentCourse:
            raise HTTPException(status_code=404,detail="Kayıtlı ders eşleşmeleri bulunamadı")
      return db_studentCourse

@app.get("/studentCourse_by_id/{studentCourse_id}",response_model=schemas.StudentCourseResponse)
async def student_course(studentCourse_id:int,db:Session=Depends(get_db)):   
      student_course=db.query(models.StudentCourse).filter(models.StudentCourse.id==studentCourse_id).first()
      if not student_course:
            raise HTTPException(status_code=404,detail="Kayıtlı ders eşleşmesi bulunamadı ")
      return student_course

@app.post("/studentCourse/",response_model=schemas.StudentCourseResponse)
async def post_studentCourse(studentCourse:schemas.StudentCourseCreate,db:Session=Depends(get_db)):
      student_id_check=db.query(models.Student).filter(models.Student.id==studentCourse.student_id).first()     
      if not student_id_check:
            raise HTTPException(status_code=404,detail="Kayıtlı öğrenci id bulunamadı")
      course_id_check=db.query(models.Course).filter(models.Course.id==studentCourse.course_id).first()
      if not course_id_check:
            raise HTTPException(status_code=404,detail="Kayıtlı ders id bulunamadı")           
      db_studentCourse=models.StudentCourse(student_id=studentCourse.student_id,course_id=studentCourse.course_id)
      db.add(db_studentCourse)
      db.commit()
      db.refresh(db_studentCourse)
      return db_studentCourse

@app.delete("/studentCourse/{studentCourse_id}")
async def delete_studentCourse(studentCourse_id:int,db:Session=Depends(get_db)):
      db_student_course=db.query(models.StudentCourse).filter(models.StudentCourse.id==studentCourse_id).first()
      if not db_student_course:
            raise HTTPException(status_code=404,detail="Eşleşme bulunamadı")
      db.delete(db_student_course)
      db.commit()
      return f"{studentCourse_id}'idli eşleşme silindi"
                         


