from sqlalchemy.orm import Session
from . import models, schemas
from .security import get_password_hash, verify_password, create_access_token, create_refresh_token

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, password_hash=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if user.password:
        db_user.password_hash = get_password_hash(user.password)
    if user.email:
        db_user.email = user.email
    if user.role:
        db_user.role = user.role
    if user.is_active is not None:
        db_user.is_active = user.is_active
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user

def create_token(db: Session, user_id: int):
    access_token = create_access_token({"sub": user_id})
    refresh_token = create_refresh_token({"sub": user_id})
    db_token = models.Token(user_id=user_id, access_token=access_token, refresh_token=refresh_token)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

def get_token(db: Session, user_id: int):
    return db.query(models.Token).filter(models.Token.user_id == user_id).first()
