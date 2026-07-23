from app.models.student_course import  StudentCourse
from app.schemas.course import  CourseResponse,CourseCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.semester import Semester
from app.models.attendance import Attendance
from app.schemas.attendances import AttendancesResponse,CreateAttendances

def get_attendances(db:Session,student_course_id:int|None=None):
  db_attendances=db.query(Attendance)  
  if student_course_id:
    db_attendances=db.query(Attendance).filter(Attendance.student_course_id==student_course_id)    
  return db_attendances.all() 


def get_attendances_by_id(db:Session,student_course_id:int):
    db_attendances=db.query(Attendance).filter(Attendance.student_course_id==student_course_id).first()  
    if not db_attendances:
       raise HTTPException(status_code=404,detail="Devamsızlık bilgisi bulunamadı")
    return db_attendances

def post_attendances(db:Session,attendancesc:CreateAttendances):
    student_course_check=db.query(StudentCourse).filter(StudentCourse.id==attendancesc.student_course_id).first()
    if not student_course_check:
       raise HTTPException(status_code=404,detail=f"{attendancesc.student_course_id}  bu student_course id sistemde bulunamadı.")
    check_duplicate=db.query(Attendance).filter(attendancesc.student_course_id==Attendance.student_course_id,attendancesc.date==Attendance.date).all()
    if check_duplicate: 
       raise HTTPException(status_code=400,detail="Sistemde zaten mevcut devamszıklık girişi var.")
    try:
        db_attendance=Attendance(student_course_id=attendancesc.student_course_id,date=attendancesc.date,is_present=attendancesc.is_present)
        db.add(db_attendance)
        db.commit()
        db.refresh(db_attendance)    
        return db_attendance
    except Exception as e:
       db.rollback()
       raise HTTPException(status_code=500,detail="Devamsızlık bilgisi yüklnemedi")
    
def put_attendances(db:Session,attendancesc:CreateAttendances,attendances_id:int):
    student_course_check=db.query(StudentCourse).filter(StudentCourse.id==attendancesc.student_course_id).first()
    if not student_course_check:
       raise HTTPException(status_code=404,detail=f"{attendancesc.student_course_id}  bu student_course id sistemde bulunamadı.")
    check_duplicate=db.query(Attendance).filter(Attendance.student_course_id==attendancesc.student_course_id,Attendance.date==attendancesc.date,Attendance.id!=attendances_id).all()
    if check_duplicate:
        raise HTTPException(status_code=400,detail="Hali hazırda sistemde zaten bu devamsızlık kayıtı var.")
    db_attendances=db.query(Attendance).filter(Attendance.id==attendances_id).first()
    if not db_attendances:
       raise HTTPException("Aradığınız id'de bir devamsızlık kayıtı yok.")
    db_attendances.student_course_id=attendancesc.student_course_id
    db_attendances.date=attendancesc.date
    db_attendances.is_present=attendancesc.is_present
    try:
       db.commit()
       db.refresh(db_attendances)
       return db_attendances
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail="Devamsızlık bilgisi güncellenmedi")
    
def delete_attendances(db:Session,attendances_id):
    db_attendances=db.query(Attendance).filter(Attendance.id==attendances_id).first()
    if  not db_attendances:
       raise HTTPException(status_code=404,detail="Devamsızlık bilgisi bulunamadı")
    try:
        db.delete(db_attendances)
        db.commit()
        return f"{attendances_id}'idli devamsızlık bilgisi silindi"
    except Exception as e:
       db.rollback()
       raise HTTPException(status_code=500,detail="Devamsızlık bilgisi silinemedi")
    
