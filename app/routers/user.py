from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.user import UserCreate,UserResponse
from app.services import user

router=APIRouter(prefix="/user",tags=["Users"])

@router.post("/",response_model=UserResponse)
def post_user(userc:UserCreate,db:Session=Depends(get_db)):
    return user.create_user(db,userc)

@router.post("/login")
def login_user(userc:UserCreate,db:Session=Depends(get_db)):
    return user.login_user(db,userc)


