"""
Exercise 3: Average Calculator with *args (Medium)

Write a function `average(*numbers)` that returns the average of any
number of arguments passed to it. If no arguments are passed, return 0
instead of raising a division-by-zero error.
"""


def average(*numbers):
    # TODO: compute and return the average of `numbers`
    # TODO: handle the empty case by returning 0
    pass


if __name__ == "__main__":
    print(average(1, 2, 3))       # expected: 2.0
    print(average(10, 20))        # expected: 15.0
    print(average())              # expected: 0
