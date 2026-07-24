from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserResponse,UserCreate
from app.security import hash_password,verify_password,create_access_token,decode_access_token


def create_user(db:Session,user:UserCreate):
    check_user_name=db.query(User).filter(User.username==user.username).all()
    if check_user_name:
        raise HTTPException(status_code=400,detail="Kullanıcı adı zaten alınmış")
    try:
        db_user=User(username=user.username,hashed_password=hash_password(user.password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=f"Kullanıcı kayıt edilmedi:{str(e)}")

def login_user(db:Session,username:str,password:str):
    check_username=db.query(User).filter(User.username==username).first()
    if not check_username:
        raise HTTPException(status_code=404,detail="Kayıtlı kullanıcı adı bulunamadı")
    check_password=verify_password(password,check_username.hashed_password) 
    if not check_password:
        raise HTTPException(status_code=401,detail="Şifre yanlış giriş yapılmadı")   

    token=create_access_token({"sub":check_username.username})
    return {"access_token":token,"token_type":"bearer"} 

