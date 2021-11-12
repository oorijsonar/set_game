from enum import Enum, auto


class TripleValueEnum(Enum):

    @classmethod
    def get_set_completing_value(cls, value1, value2):
        if value1 == value2:
            return value1
        return (set(cls) - {value1, value2}).pop()


class Color(TripleValueEnum):
    GREEN = auto()
    PURPLE = auto()
    RED = auto()


class Number(TripleValueEnum):
    ONE = auto()
    TWO = auto()
    THREE = auto()


class Shading(TripleValueEnum):
    SOLID = auto()
    STRIPED = auto()
    OPEN = auto()


class Shape(TripleValueEnum):
    DIAMOND = auto()
    SQUIGGLE = auto()
    OVAL = auto()
