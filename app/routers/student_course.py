from app.services import student_course
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db,get_current_user,get_current_admin_user
from app.models.user import User
from app.schemas.student_course import StudentCourseCreate, StudentCourseResponse
from app.schemas.attendances import AttendancesResponse


router=APIRouter(prefix="/student_course",tags=["Student with courses"])

@router.get("/",response_model=list[StudentCourseResponse])
def get_student_course_all(db:Session=Depends(get_db),student_id:int|None=None,course_id:int|None=None,current_user:dict=Depends(get_current_user)):
    return student_course.get_student_course(db,student_id,course_id)

@router.get("/attendances",response_model=list[AttendancesResponse])
def get_student_course_attendances(student_id:int,course_id:int,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    return student_course.get_student_course_attendance(db,student_id,course_id)

@router.get("/{student_course_id}",response_model=StudentCourseResponse)
def get_student_course_by_id(student_course_id:int,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    return student_course.get_student_course_by_id(student_course_id,db)

@router.post("/",response_model=StudentCourseResponse)
def post_student_course(student_coursec:StudentCourseCreate,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    return student_course.post_student_course(student_coursec,db)

@router.put("/{student_course_id}",response_model=StudentCourseResponse)
def put_student_course(student_coursec:StudentCourseCreate,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    return student_course.put_student_course(student_coursec,db)

@router.delete("/{student_course_id}")
def delete_student_course(student_course_id:int,db:Session=Depends(get_db),admin:dict=Depends(get_current_admin_user)):
    return student_course.delete_student_course(student_course_id,db)

