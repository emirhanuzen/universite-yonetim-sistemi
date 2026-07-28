from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db,get_current_user,get_current_admin_user
from app.models.user import User
from app.schemas.teacher import TeacherCreate, TeacherResponse,TeacherWithCoursesResponse
from app.schemas.course import CourseResponse
from app.services import teacher
 

router=APIRouter(prefix="/teacher",tags=["teacher"])

@router.get("/",response_model=list[TeacherResponse])
def get_teacher(db:Session=Depends(get_db),title:str|None=None,department:str|None=None,name:str |None=None,current_user:dict=Depends(get_current_user)):
    return teacher.get_teacher(db,title,department,name)

@router.get("/{teacher_id}",response_model=TeacherResponse)
def get_by_id_teacher(teacher_id:int,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    return teacher.get_teacher_by_id(teacher_id,db)

@router.get("/with_course/{teacher_id}",response_model=TeacherWithCoursesResponse)
def get_teacher_with_course(teacher_id:int,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    return teacher.get_teacher_with_course(teacher_id,db)

@router.post("/",response_model=TeacherResponse)
def post_teacher(teacherc:TeacherCreate,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    return teacher.post_teacher(teacherc,db)

@router.put("/{teacher_id}",response_model=TeacherResponse)
def put_teacher(teacher_id:int,teacherc:TeacherCreate,db:Session=Depends(get_db),current_user:dict=Depends(get_current_user)):
    return teacher.put_teacher(teacher_id,teacherc,db)

@router.delete("/{teacher_id}")
def delete_teacher(teacher_id:int,db:Session=Depends(get_db),admin:User=Depends(get_current_admin_user)):
    return teacher.delete_teacher(teacher_id,db)
