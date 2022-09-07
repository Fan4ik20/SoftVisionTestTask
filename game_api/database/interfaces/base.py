from sqlalchemy.orm import Session

from database.models import GameBase


class InterfaceBase:
    @staticmethod
    def create(db: Session, *args) -> GameBase:
        raise NotImplementedError

    @staticmethod
    def get(db: Session, *args) -> GameBase | None:
        raise NotImplementedError

    @staticmethod
    def get_list(db: Session, *args) -> list[GameBase]:
        raise NotImplementedError

    @staticmethod
    def delete(db: Session, *args) -> None:
        raise NotImplementedError
