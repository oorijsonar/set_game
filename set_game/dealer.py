import itertools
import random
from card import Card
from features import Color, Number, Shading, Shape

INITIAL_BOARD_SIZE = 12


def generate_deck():
    return [Card(*combo) for combo in itertools.product(Color, Number, Shading, Shape)]


def deal(deck=None):
    if deck is None:
        deck = generate_deck()
    return random.sample(deck, INITIAL_BOARD_SIZE)

