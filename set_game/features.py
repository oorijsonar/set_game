from enum import Enum, auto


class Color(Enum):
    GREEN = auto()
    PURPLE = auto()
    RED = auto()


class Number(Enum):
    ONE = auto()
    TWO = auto()
    THREE = auto()


class Shading(Enum):
    SOLID = auto()
    STRIPED = auto()
    OPEN = auto()


class Shape(Enum):
    DIAMOND = auto()
    SQUIGGLE = auto()
    OVAL = auto()
