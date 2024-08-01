from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, security, dependencies

router = APIRouter()

@router.post("/login", response_model=schemas.TokenInDB)
def login(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if not db_user or not security.verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = crud.create_token(db, db_user.id)
    return token

@router.post("/token/refresh", response_model=schemas.TokenInDB)
def refresh_token(refresh_token: str, db: Session = Depends(dependencies.get_db)):
    payload = security.verify_token(refresh_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    user_id = payload.get("sub")
    db_token = crud.get_token(db, user_id=user_id)
    if not db_token:
        raise HTTPException(status_code=404, detail="Token not found")
    new_access_token = security.create_access_token({"sub": user_id})
    db_token.access_token = new_access_token
    db.commit()
    return db_token
