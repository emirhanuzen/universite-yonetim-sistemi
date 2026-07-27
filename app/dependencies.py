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
    if username is None:
        raise HTTPException(status_code=401, detail="Gecersiz token")
    return username

def get_current_admin_user(username:str=Depends(get_current_user),db:Session=Depends(get_db) ):
    db_user=db.query(User).filter(User.username==username).first()
    if not  db_user:
        raise HTTPException(status_code=404,detail="Kullanıcı bulunamadı")
    if db_user.role!="admin":
        raise HTTPException(status_code=403,detail="Yetkisiz işlem.")
    return db_user
    
      
