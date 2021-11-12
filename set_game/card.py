from textwrap import dedent

from features import Color, Number, Shading, Shape


class Card:

    def __init__(self, color: Color, number: Number, shading: Shading, shape: Shape):
        self.color = color
        self.number = number
        self.shading = shading
        self.shape = shape

    def __eq__(self, other):
        return (self.color == other.color and
                self.number == other.number and
                self.shading == other.shading and
                self.shape == other.shape)

    def __repr__(self):
        return dedent(
            f'''
            Color: {self.color.name}
            Number: {self.number.name}
            Shading: {self.shading.name}
            Shape: {self.shape.name}
            '''
        )
