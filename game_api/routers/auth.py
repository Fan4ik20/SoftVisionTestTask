from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT

from sqlalchemy.orm import Session

from database.interfaces.user_interface import UserInterface

from dependencies.stubs import GameDb

from schemas.user_sch import UserCreate, User, UserLogin

from exceptions import exc

router = APIRouter(tags=['Authentication'])


@router.post(
    '/register/', response_model=User, status_code=status.HTTP_201_CREATED
)
def register(user: UserCreate, db: Session = Depends(GameDb)):
    if UserInterface.get_by_name(db, user.name):
        raise exc.ObjectWithGivenAttrExist('User', 'name')
    if UserInterface.get_by_email(db, user.email):
        raise exc.ObjectWithGivenAttrExist('User', 'email')

    return UserInterface.create(db, user)


@router.post('/login/')
def login(
        user: UserLogin,
        db: Session = Depends(GameDb), auth: AuthJWT = Depends()
):
    db_user = UserInterface.get_by_name(db, user.name)

    if db_user is None:
        raise exc.NotValidLoginData('name')
    if db_user.email != user.email:
        raise exc.NotValidLoginData('email')

    access_token = auth.create_access_token(subject=user.name)

    return {'access_token': access_token}
