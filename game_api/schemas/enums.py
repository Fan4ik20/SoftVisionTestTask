from enum import Enum


class AvailablePlaces(str, Enum):
    body = 'Body'
    query = 'Query'
    path = 'Path'
