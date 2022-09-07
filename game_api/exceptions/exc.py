class ObjectWithGivenAttrExist(Exception):
    def __init__(self, object_name: str, attr: str) -> None:
        self.name = object_name
        self.attr = attr


class NotValidLoginData(Exception):
    def __init__(self, attr: str) -> None:
        self.attr = attr
