from sqlalchemy import select
from sqlalchemy.sql.selectable import Select
from sqlalchemy.orm import Session, selectinload

from database.models import Game, User

from schemas.game_sch import GameCreate

from .base import InterfaceBase


class GameInterface(InterfaceBase):
    @staticmethod
    def create(db: Session, game_sch: GameCreate) -> Game:
        game = Game(**game_sch.dict())

        db.add(game)
        db.commit()

        db.refresh(game)

        return game

    @staticmethod
    def get(db: Session, game_id: int) -> Game | None:
        return db.get(Game, game_id)

    @staticmethod
    def get_by_name(db: Session, name: str) -> Game | None:
        return db.scalar(
            select(Game).filter_by(name=name)
        )

    @staticmethod
    def _select_list(offset: int = 0, limit: int = 100) -> Select:
        return select(Game).offset(offset).limit(limit)

    @staticmethod
    def get_list(db: Session, offset: int = 0, limit: int = 100) -> list[Game]:
        return db.scalars(
            GameInterface._select_list(offset, limit)
        )

    @staticmethod
    def get_list_with_users(
            db: Session, offset: int = 0, limit: int = 100
    ) -> list[Game]:
        return db.scalars(
            GameInterface._select_list(offset, limit).options(
                selectinload(Game.users)
            )
        ).all()

    @staticmethod
    def delete(db: Session, game: Game) -> None:
        db.delete(game)

        db.commit()

    @staticmethod
    def add_user(db: Session, game: Game, user: User) -> None:
        game.users.append(user)
        db.commit()

    @staticmethod
    def remove_user(db: Session, game: Game, user: User) -> None:
        game.users.remove(user)
        db.commit()
