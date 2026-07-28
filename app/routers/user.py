from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db,get_current_user,get_current_admin_user
from app.schemas.user import UserCreate,UserResponse
from app.services import user
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import User

router=APIRouter(prefix="/user",tags=["Users"])

@router.post("/",response_model=UserResponse)
def post_user(userc:UserCreate,db:Session=Depends(get_db)):
    return user.create_user(db,userc)

@router.post("/login")
def login_user(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    return user.login_user(db,form_data.username,form_data.password)

@router.put("/promote/{user_id}",response_model=UserResponse)
def promote_user(user_id:int,db:Session=Depends(get_db),admin:User=Depends(get_current_admin_user)):
    return user.promote_user(user_id,db)

@router.put("/demote/{user_id}",response_model=UserResponse)
def demote_user(user_id:int,db:Session=Depends(get_db),admin:User=Depends(get_current_admin_user)):
    return user.demote_user(user_id,db)

@router.delete("/{user_id}")
def delete_user(user_id:int,db:Session=Depends(get_db),admin:User=Depends(get_current_admin_user)):
    return user.delete_user(user_id,db)

@router.get("/",response_model=list[UserResponse])
def get_user(username:str|None=None,db:Session=Depends(get_db),admin:User=Depends(get_current_admin_user)):
    return user.get_user(db,username)

@router.put("/user_set_role",response_model=UserResponse)
def user_set_role(user_id:int,new_role:str,db:Session=Depends(get_db),admin:dict=Depends(get_current_admin_user)):
    return user.user_set_role(user_id,new_role,db)