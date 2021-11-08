import itertools
from abc import ABC, abstractmethod
from typing import Union

from card import Card
from dealer import INITIAL_BOARD_SIZE
from triplet import Triplet

ADDITIONAL_CARDS_DEALT = 3


class Algorithm(ABC):

    def __init__(self, board: list[Card]):
        assert len(board) >= INITIAL_BOARD_SIZE, f'Must have at least {INITIAL_BOARD_SIZE} cards on the board!'
        assert len(
            board) % ADDITIONAL_CARDS_DEALT == 0, f'Can only add cards to the board in increments of {ADDITIONAL_CARDS_DEALT}!'
        self.board = board

    @abstractmethod
    def find(self) -> Union[Triplet, None]:
        pass


class BruteForce(Algorithm):

    def find(self) -> Union[Triplet, None]:
        triplets = itertools.starmap(Triplet, itertools.combinations(self.board, 3))

        for triplet in triplets:
            if triplet.is_set():
                return triplet

        return None
