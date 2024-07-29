from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    role: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str | None = None
    is_active: bool | None = None

class UserInDB(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True