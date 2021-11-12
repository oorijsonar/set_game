import itertools
from abc import ABC, abstractmethod
from typing import Union

from card import Card
from dealer import INITIAL_BOARD_SIZE
from features import Color, Number, Shading, Shape
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


class SetCompleter(Algorithm):

    def find(self) -> Union[Triplet, None]:
        if len(self.board) < 3:
            return None

        first_card = self.board.pop()
        index_of_last_candidate = len(self.board) - 1  # the last card on the board can't be the second card in the set

        for second_card in self.board[:index_of_last_candidate]:

            set_completer = self._find_set_completer(first_card, second_card)

            if set_completer in self.board:
                return Triplet(first_card, second_card, set_completer)

        return self.find()

    def _find_set_completer(self, card1, card2):
        color = Color.get_set_completing_value(card1.color, card2.color)
        number = Number.get_set_completing_value(card1.number, card2.number)
        shading = Shading.get_set_completing_value(card1.shading, card2.shading)
        shape = Shape.get_set_completing_value(card1.shape, card2.shape)
        return Card(color, number, shading, shape)
