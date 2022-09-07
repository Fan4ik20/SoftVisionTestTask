from typing import Callable

from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from sqlalchemy.orm import sessionmaker, Session

from database import models
from database.interfaces.user_interface import UserInterface

from .stubs import GameDb


def get_db_session(sessionmaker_: sessionmaker) -> Callable:
    def get_session():
        with sessionmaker_() as session:
            yield session
    return get_session


def login_required(auth: AuthJWT = Depends()) -> None:
    auth.jwt_required()


def get_current_user(
        auth: AuthJWT = Depends(),
        db: Session = Depends(GameDb),
        _=Depends(login_required)
) -> models.User:
    name = auth.get_jwt_subject()

    user = UserInterface.get_by_name(db, name)

    return user


class PaginationParams:
    def __init__(self, offset: int = 0, limit: int = 100):
        self.offset = offset
        self.limit = limit
