import itertools

from card import Card
from features import Color, Number, Shading, Shape


def generate():
    return [Card(*combo) for combo in itertools.product(Color, Number, Shading, Shape)]
