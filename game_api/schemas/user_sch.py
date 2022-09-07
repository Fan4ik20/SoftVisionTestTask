from typing import TypeAlias

from pydantic import BaseModel, EmailStr, PositiveInt, Field, validator

identifier: TypeAlias = PositiveInt


class UserBase(BaseModel):
    name: str = Field(..., max_length=50)
    email: EmailStr
    age: int = Field(..., lt=100, gt=1)


class UserLogin(BaseModel):
    name: str = Field(..., max_length=50)
    email: EmailStr


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: identifier

    class Config:
        orm_mode = True
