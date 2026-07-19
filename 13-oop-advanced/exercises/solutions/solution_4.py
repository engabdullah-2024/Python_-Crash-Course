# Solution to Exercise 4: Alternative constructors

import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    @classmethod
    def square(cls, side):
        return cls(side, side)

    @classmethod
    def from_diagonal(cls, diagonal):
        side = diagonal / math.sqrt(2)
        return cls(side, side)

    @staticmethod
    def is_valid_dimension(value):
        return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


if __name__ == "__main__":
    sq = Rectangle.square(4)
    print(sq.width, sq.height, sq.area())          # 4 4 16

    diag_sq = Rectangle.from_diagonal(math.sqrt(2) * 5)
    print(round(diag_sq.width, 4), round(diag_sq.height, 4))  # 5.0 5.0

    print(Rectangle.is_valid_dimension(5))     # True
    print(Rectangle.is_valid_dimension(-2))     # False
    print(Rectangle.is_valid_dimension("5"))     # False
