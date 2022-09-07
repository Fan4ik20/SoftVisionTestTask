from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, validates


GameBase = declarative_base()


class User(GameBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    age = Column(Integer)

    game_id = Column(Integer, ForeignKey('games.id'))

    @validates('age')
    def validate_age(self, _, value: int):
        if not 1 <= value <= 100:
            raise ValueError('Age must be in the range of 1 to 100')
        return value


class Game(GameBase):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
