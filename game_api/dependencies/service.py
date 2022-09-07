from typing import Callable

from sqlalchemy.orm import sessionmaker


def get_db_session(sessionmaker_: sessionmaker) -> Callable:
    def get_session():
        with sessionmaker_() as session:
            yield session
    return get_session


class PaginationParams:
    def __init__(self, offset: int = 0, limit: int = 100):
        self.offset = offset
        self.limit = limit
