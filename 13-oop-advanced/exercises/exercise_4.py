"""
Exercise 4 (Medium): Alternative constructors

Extend the `Rectangle` class below with:
  - a @classmethod `square(cls, side)` that returns a Rectangle with
    width == height == side
  - a @classmethod `from_diagonal(cls, diagonal)` that returns a *square*
    Rectangle whose diagonal equals the given value
    (hint: for a square, diagonal = side * sqrt(2), so side = diagonal / sqrt(2))
  - a @staticmethod `is_valid_dimension(value)` that returns True if value
    is a positive number (int or float), False otherwise
"""

import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    # TODO: add square() classmethod

    # TODO: add from_diagonal() classmethod

    # TODO: add is_valid_dimension() staticmethod


if __name__ == "__main__":
    sq = Rectangle.square(4)
    print(sq.width, sq.height, sq.area())

    diag_sq = Rectangle.from_diagonal(math.sqrt(2) * 5)
    print(round(diag_sq.width, 4), round(diag_sq.height, 4))

    print(Rectangle.is_valid_dimension(5))
    print(Rectangle.is_valid_dimension(-2))
    print(Rectangle.is_valid_dimension("5"))
