from database.models import GameBase


class InterfaceBase:
    @staticmethod
    def create(*args) -> GameBase:
        raise NotImplementedError

    @staticmethod
    def get(*args) -> GameBase:
        raise NotImplementedError

    @staticmethod
    def get_list(*args) -> list[GameBase]:
        raise NotImplementedError

    @staticmethod
    def delete(*args) -> None:
        raise NotImplementedError
