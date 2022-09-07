from sqlalchemy import select
from sqlalchemy.orm import Session

from database.models import User

from schemas.user_sch import UserCreate

from .base import InterfaceBase


class UserInterface(InterfaceBase):
    @staticmethod
    def create(db: Session, user_sch: UserCreate) -> User:
        db_user = User(**user_sch.dict())

        db.add(db_user)
        db.commit()

        db.refresh(db_user)

        return db_user

    @staticmethod
    def get(db: Session, user_id: int) -> User:
        return db.get(User, user_id)

    @staticmethod
    def get_by_name(db: Session, name: str) -> User | None:
        return db.scalar(
            select(User).filter_by(name=name)
        )

    @staticmethod
    def get_by_email(db: Session, email: str) -> User | None:
        return db.scalar(
            select(User).filter_by(email=email)
        )

    @staticmethod
    def get_list(db: Session, offset: int = 0, limit: int = 100) -> list[User]:
        return db.scalars(
            select(User).offset(offset).limit(limit)
        ).all()

    @staticmethod
    def delete(db: Session, user: User) -> None:
        db.delete(user)
        db.commit()
