from typing import TypeAlias

from pydantic import BaseModel, PositiveInt, Field

from .user_sch import UserBuiltin


identifier: TypeAlias = PositiveInt


class GameBase(BaseModel):
    name: str = Field(..., max_length=100)


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: identifier

    class Config:
        orm_mode = True


class GameDetail(GameBase):
    id: identifier

    users: list[UserBuiltin]

    class Config:
        orm_mode = True
