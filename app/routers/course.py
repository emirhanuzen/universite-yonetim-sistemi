from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db,get_current_user,get_current_admin_user
from app.models.user import User
from app.schemas.student import StudentCreate, StudentResponse
from app.schemas.teacher import TeacherCreate, TeacherResponse
from app.schemas.course import CourseResponse,CourseCreate
from app.schemas.semester import  SemesterResponse
from app.services import teacher
from app.services import course

router=APIRouter(prefix="/course",tags=["courses"])

@router.get("/",response_model=list[CourseResponse])
def get_all_course(db:Session=Depends(get_db),name:str|None=None,teacher_id:int|None=None,semester_id:int|None=None,current_user:dict=Depends(get_current_user)):
    return course.get_course(db,name,teacher_id,semester_id)    

@router.get("/{course_id}",response_model=CourseResponse)
def get_by_id_course(course_id:int,db:Session=Depends(get_db),curretn_user:dict=Depends(get_current_user)):
    return course.get_course_by_id(course_id,db)

@router.get("/with_teacher/{course_id}",response_model=TeacherResponse)
def get_with_teacher(course_id:int,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    return course.get_course_with_teacher(course_id,db)

@router.post("/",response_model=CourseResponse)
def post_course(courseC:CourseCreate,db:Session=Depends(get_db),admin:dict=Depends(get_current_admin_user)):
    return course.post_course(courseC,db)

@router.put("/{course_id}",response_model=CourseResponse)
def put_course(course_id:int,courseC:CourseCreate,db:Session=Depends(get_db),admin:dict=Depends(get_current_admin_user)):
    return course.put_course(course_id,courseC,db)

@router.delete("/{course_id}")
def delete_course(course_id:int,db:Session=Depends(get_db),admin:dict=Depends(get_current_admin_user)):
    return course.delete_course(course_id,db)

@router.get("/course_with_students/{course_id}",response_model=list[StudentResponse])
def get_with_students(course_id:int,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    return course.get_course_with_student(course_id,db)

@router.get("/course_only_semester/{course_id}",response_model=SemesterResponse)
def get_with_semester(course_id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    return course.get_course_semester(course_id,db)






