import random

from algorithm import BruteForce
from deck import generate

INITIAL_BOARD_SIZE = 12


def main():
    deck = generate()
    board = random.sample(deck, INITIAL_BOARD_SIZE)
    print(BruteForce(board).find())


if __name__ == '__main__':
    main()
