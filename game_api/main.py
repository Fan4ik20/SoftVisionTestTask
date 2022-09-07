from fastapi import FastAPI

from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi_jwt_auth import AuthJWT

from database.settings import create_engine, create_sessionmaker
from database.interfaces.db_service import DbInterface

from config import DatabaseSettings, SecuritySettings

from dependencies.stubs import GameDb
from dependencies.service import get_db_session

from exceptions import exc, handlers

from routers import game_router


def include_db(app: FastAPI, config: DatabaseSettings) -> None:
    game_engine = create_engine(config)
    game_sessionmaker = create_sessionmaker(game_engine)

    DbInterface.create_tables(game_engine)

    app.dependency_overrides[GameDb] = get_db_session(game_sessionmaker)


def include_router(app: FastAPI) -> None:
    app.include_router(game_router.router, prefix='/api/v1')


def include_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        exc.ObjectWithGivenAttrExist,
        handlers.object_with_given_attr_exist_handler
    )
    app.add_exception_handler(
        AuthJWTException, handlers.authjwt_exception_handler
    )
    app.add_exception_handler(
        exc.NotValidLoginData, handlers.not_valid_login_data_handler
    )


def create_app() -> FastAPI:
    app = FastAPI(docs_url='/api/v1/docs/')

    db_config = DatabaseSettings(_env_file='.env')

    include_db(app, db_config)
    include_router(app)

    return app


@AuthJWT.load_config
def get_secure_config():
    return SecuritySettings(_env_file='.env')


game_api = create_app()
