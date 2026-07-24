from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db,get_current_user
from app.schemas.attendances import AttendancesResponse,CreateAttendances
from app.schemas.student_course import StudentCourseCreate,StudentCourseResponse
from app.schemas.course import CourseResponse,CourseCreate
from app.schemas.semester import  SemesterResponse
from app.services import attendances
from app.models.student_course import StudentCourse

router=APIRouter(prefix="/attendances",tags=["attendances"])


@router.get("/",response_model=list[AttendancesResponse])
def get_attendances(db:Session=Depends(get_db),attendances_id:int|None=None,current_user:str=Depends(get_current_user)):
    return attendances.get_attendances(db,attendances_id)

@router.get("/{attendances_id}",response_model=AttendancesResponse)
def get_attendances_by_id(db:Session=Depends(get_db),attendances_id:int|None=None,current_user:str=Depends(get_current_user)):
    return attendances.get_attendances_by_id(db,attendances_id)

@router.post("/",response_model=AttendancesResponse)
def post_attendances(attendancesc:CreateAttendances,db:Session=Depends(get_db),current_user:str=Depends(get_current_user)):
    return attendances.post_attendances(db,attendancesc)

@router.put("/{attendances_id}",response_model=AttendancesResponse)
def put_attendances(attendances_id:int,attendancesc:CreateAttendances,db:Session=Depends(get_db),current_user:str=Depends(get_current_user)):
    return attendances.put_attendances(db,attendancesc,attendances_id)

@router.delete("/{attendances_id}")
def delete_attendances(attendances_id:int,db:Session=Depends(get_db),current_user:str=Depends(get_current_user)):
    return attendances.delete_attendances(db,attendances_id)
