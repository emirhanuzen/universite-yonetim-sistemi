from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db,get_current_user
from app.schemas.student import StudentCreate, StudentResponse
from app.schemas.course import CourseResponse
from app.services import student

router=APIRouter(prefix="/student",tags=["students"])

@router.get("/",response_model=list[StudentResponse])
def get_all_student(db:Session=Depends(get_db),name:str|None=None,no:str|None=None,current_user=Depends(get_current_user)):
    return student.get_student(db,name,no)

@router.get("/{student_id}",response_model=StudentResponse)
def get_by_id(student_id:int,db:Session=Depends(get_db),current_user:str=Depends(get_current_user)):
    return student.get_student_by_id(student_id,db)

@router.post("/",response_model=StudentResponse)
def post_student(studentc:StudentCreate,db:Session=Depends(get_db),current_user:str=Depends(get_current_user)):
    return student.post_student(studentc,db)

@router.put("/{student_id}",response_model=StudentResponse)
def put_student(student_id:int,studentc:StudentCreate,db:Session=Depends(get_db),current_user:str=Depends(get_current_user)):
    return student.put_student(student_id,studentc,db)

@router.delete("/{stduent_İd}")
def delete_student(student_id:int,db:Session=Depends(get_db),current_user:str=Depends(get_current_user)):
    return student.delete_student(student_id,db)

@router.get("/get_with_courses/{student_id}",response_model=list[CourseResponse])
def get_with_courses(student_id:int,db:Session=Depends(get_db),current_user:str=Depends(get_current_user)):
    return student.get_with_courses(student_id,db)


