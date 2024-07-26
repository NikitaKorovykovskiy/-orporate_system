from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str
    role: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None
    is_active: Optional[bool] = None

class UserInDB(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class TokenBase(BaseModel):
    access_token: str
    refresh_token: str

class TokenCreate(TokenBase):
    user_id: int

class TokenInDB(TokenBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True