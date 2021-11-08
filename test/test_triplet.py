import pytest

from set_game.card import Card
from set_game.features import Color, Number, Shading, Shape
from set_game.triplet import Triplet

IS_SET_PARAMETERS = [
    (Triplet(Card(Color.RED, Number.ONE, Shading.OPEN, Shape.OVAL),
             Card(Color.RED, Number.TWO, Shading.OPEN, Shape.OVAL),
             Card(Color.RED, Number.THREE, Shading.OPEN, Shape.OVAL)), True),

    (Triplet(Card(Color.RED, Number.ONE, Shading.OPEN, Shape.OVAL),
             Card(Color.PURPLE, Number.ONE, Shading.STRIPED, Shape.DIAMOND),
             Card(Color.GREEN, Number.ONE, Shading.SOLID, Shape.SQUIGGLE)), True),

    (Triplet(Card(Color.PURPLE, Number.ONE, Shading.OPEN, Shape.OVAL),
             Card(Color.RED, Number.TWO, Shading.OPEN, Shape.OVAL),
             Card(Color.RED, Number.THREE, Shading.OPEN, Shape.OVAL)), False)
]


@pytest.mark.parametrize('triplet, expected', IS_SET_PARAMETERS)
def test_is_set(triplet, expected):
    assert triplet.is_set() == expected
