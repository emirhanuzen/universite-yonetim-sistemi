from app.db.database import SessionLocal,sessionmaker
from sqlalchemy.orm import Session
from app.models.user import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    username = payload.get("sub")
    role=payload.get("role")
    if username is None:
        raise HTTPException(status_code=403, detail="Gecersiz token")
    return {"username":username,"role":role}

def get_current_admin_user(current_user:dict=Depends(get_current_user)):
    if current_user["role"]!="admin":
         raise HTTPException(status_code=403, detail="Yetkisiz işlem")
    return current_user    
    
      
