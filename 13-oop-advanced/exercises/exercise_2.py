"""
Exercise 2 (Medium): Custom Money dunder methods

Implement a `Money` class that wraps an integer number of cents so that
arithmetic is exact (avoiding float rounding issues).

Requirements:
  - __init__(self, dollars, cents=0) stores self.total_cents = dollars * 100 + cents
  - __repr__ returns something like "Money(19, 99)"
  - __str__ returns something like "$19.99" (always 2 decimal places)
  - __eq__ compares two Money objects by total_cents
  - __add__ returns a new Money object representing the sum
    (hint: you can construct the result from total cents via
    Money(0, combined_cents) since cents can exceed 99 internally)
"""


class Money:
    def __init__(self, dollars, cents=0):
        # TODO: store self.total_cents
        pass

    def __repr__(self):
        # TODO
        pass

    def __str__(self):
        # TODO: format as $D.CC
        pass

    def __eq__(self, other):
        # TODO
        pass

    def __add__(self, other):
        # TODO
        pass


if __name__ == "__main__":
    price = Money(19, 99)
    tax = Money(1, 60)
    total = price + tax

    print(repr(price))
    print(price)
    print(total)
    print(price == Money(19, 99))
