from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db,get_current_user
from app.schemas.user import UserCreate,UserResponse
from app.services import user
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(prefix="/user",tags=["Users"])

@router.post("/",response_model=UserResponse)
def post_user(userc:UserCreate,db:Session=Depends(get_db)):
    return user.create_user(db,userc)

@router.post("/login")
def login_user(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    return user.login_user(db,form_data.username,form_data.password)


