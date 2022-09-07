from fastapi import APIRouter, Depends, Response, status

from sqlalchemy.orm import Session

from database.models import User
from database.interfaces.user_interface import UserInterface

from dependencies.stubs import ActiveUser, GameDb

router = APIRouter(prefix='/users', tags=['User'])


@router.get('/me/', response_model=User)
def get_current_user(active_user: User = Depends(ActiveUser)):
    return active_user


@router.delete(
    '/me/', response_class=Response, status_code=status.HTTP_204_NO_CONTENT
)
def delete_current_user(
        active_user: User = Depends(ActiveUser),
        db: Session = Depends(GameDb)
):
    UserInterface.delete(db, active_user)
