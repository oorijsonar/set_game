from textwrap import dedent

from card import Card


class Triplet:

    def __init__(self, card1: Card, card2: Card, card3: Card):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.triplet = (card1, card2, card3)
        self.colors = (card1.color, card2.color, card3.color)
        self.numbers = (card1.number, card2.number, card3.number)
        self.shadings = (card1.shading, card2.shading, card3.shading)
        self.shapes = (card1.shape, card2.shape, card3.shape)

    def __repr__(self):
        return dedent(
            f'''
            First card: {self.card1.color}, {self.card1.number}, {self.card1.shading}, {self.card1.shape}
            Second card: {self.card2.color}, {self.card2.number}, {self.card2.shading}, {self.card2.shape}
            Third card: {self.card3.color}, {self.card3.number}, {self.card3.shading}, {self.card3.shape}
            '''
        )

    def is_set(self):
        return all(map(self._is_set_part, (self.colors, self.numbers, self.shadings, self.shapes)))

    def _is_set_part(self, feature_list):
        feature_set = set(feature_list)
        return len(feature_set) == len(feature_list) or len(feature_set) == 1
