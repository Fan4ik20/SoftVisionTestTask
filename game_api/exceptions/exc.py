class ObjectWithGivenAttrExist(Exception):
    def __init__(self, object_name: str, attr: str) -> None:
        self.name = object_name
        self.attr = attr


class NotValidLoginData(Exception):
    def __init__(self, attr: str) -> None:
        self.attr = attr


class ObjectNotExist(Exception):
    def __init__(self, object_name: str) -> None:
        self.name = object_name


class CantPerformThis(Exception):
    def __init__(self, action: str) -> None:
        self.action = action
