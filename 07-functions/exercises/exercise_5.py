"""
Exercise 5: Scope and a Running Total (Hard)

Create a module-level variable `running_total = 0`.

Write a function `add_to_total(amount)` that uses the `global` keyword
to add `amount` to `running_total`.

Write a second function `reset_total()` that resets `running_total` back
to 0, also using `global`.

In the __main__ block, call add_to_total() a few times, print
running_total after each call, then call reset_total() and print it
again to confirm it went back to 0.
"""

running_total = 0


def add_to_total(amount):
    # TODO: use `global running_total` and add `amount` to it
    pass


def reset_total():
    # TODO: use `global running_total` and set it back to 0
    pass


if __name__ == "__main__":
    # TODO: call add_to_total a few times, printing running_total each time
    # TODO: call reset_total, then print running_total to confirm it's 0
    pass
