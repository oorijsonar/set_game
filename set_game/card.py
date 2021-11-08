from features import Color, Number, Shading, Shape


class Card:

    def __init__(self, color: Color, number: Number, shading: Shading, shape: Shape):
        self.color = color
        self.number = number
        self.shading = shading
        self.shape = shape
