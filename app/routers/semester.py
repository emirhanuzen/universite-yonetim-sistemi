
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services import semester
from app.models.semester import Semester
from app.schemas.semester import SemesterCreate,SemesterResponse
from app.schemas.course import CourseResponse

router=APIRouter(prefix="/semester",tags=["Semesters"])

@router.get("/",response_model=list[SemesterResponse])
def get_semester_all(db:Session=Depends(get_db)):
    return semester.get_semester_all(db)

@router.get("/{semester_id}",response_model=SemesterResponse)
def get_semester_by_id(semester_id:int,db:Session=Depends(get_db)):
    return semester.get_semester_by_id(semester_id,db)

@router.get("/semester_with_courses/{semester_id}",response_model=SemesterResponse)
def get_with_courses(semester_id:int,db:Session=Depends(get_db)):
    return semester.get_semester_with_courses(semester_id,db)

@router.post("/",response_model=SemesterResponse)
def post_semester(semesterc:SemesterCreate,db:Session=Depends(get_db)):
    return semester.post_semester(semesterc,db)

@router.put("/{semester_id}",response_model=SemesterResponse)
def put_semester(semester_id:int,semesterc:SemesterCreate,db:Session=Depends(get_db)):
    return semester.put_semester(semester_id,semesterc,db)

