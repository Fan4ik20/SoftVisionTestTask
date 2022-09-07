from fastapi import APIRouter, Depends, Response, status

from sqlalchemy.orm import Session

from dependencies.stubs import ActiveUser, GameDb
from dependencies.service import PaginationParams

from database import models
from database.interfaces.game_interface import GameInterface

from exceptions import exc

from schemas import game_sch

router = APIRouter(prefix='/games', tags=['Games'])


def get_game_or_raise_404_if_is_none(db: Session, game_id: int) -> models.Game:
    game = GameInterface.get(db, game_id)

    if not game:
        raise exc.ObjectNotExist('Game')

    return game


@router.get('/', response_model=list[game_sch.GameDetail])
def get_games(
        db: Session = Depends(GameDb), pagination: PaginationParams = Depends()
):
    games = GameInterface.get_list_with_users(
        db, pagination.offset, pagination.limit
    )

    return games


@router.post(
    '/', response_model=game_sch.Game, status_code=status.HTTP_201_CREATED
)
def create_game(
        game: game_sch.GameCreate, db: Session = Depends(GameDb)
):
    db_game = GameInterface.get_by_name(db, game.name)

    if db_game:
        raise exc.ObjectWithGivenAttrExist('Game', 'name')

    return GameInterface.create(db, game)


@router.get('/{game_id}/', response_model=game_sch.GameDetail)
def get_game(game_id: int, db: Session = Depends(GameDb)):
    game = get_game_or_raise_404_if_is_none(db, game_id)

    return game


@router.delete(
    '/{game_id}/', response_class=Response,
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_game(game_id: int, db: Session = Depends(GameDb)):
    game = get_game_or_raise_404_if_is_none(db, game_id)

    GameInterface.delete(db, game)


@router.post('/{game_id}/connect/')
def connect_to_game(
        game_id: int, db: Session = Depends(GameDb),
        active_user: models.User = Depends(ActiveUser)
):
    game = get_game_or_raise_404_if_is_none(db, game_id)

    if active_user in game.users:
        raise exc.CantPerformThis("You can't connect to game again")

    GameInterface.add_user(db, game, active_user)

    return {'status': 'OK'}


@router.post('/{game_id}/disconnect/')
def disconnect_from_game(
        game_id: int, db: Session = Depends(GameDb),
        active_user: models.User = Depends(ActiveUser)
):
    game = get_game_or_raise_404_if_is_none(db, game_id)

    if active_user not in game.users:
        raise exc.CantPerformThis(
            "You can't connect to game without connecting it"
        )

    GameInterface.remove_user(db, game, active_user)

    return {'status': 'OK'}
