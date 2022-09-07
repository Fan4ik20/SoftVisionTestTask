from sqlalchemy import create_engine as _create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from config import DatabaseSettings


def create_engine(config: DatabaseSettings) -> Engine:
    return _create_engine(config.DB_URL)


def create_sessionmaker(engine: Engine) -> sessionmaker:
    return sessionmaker(autoflush=False, bind=engine)
