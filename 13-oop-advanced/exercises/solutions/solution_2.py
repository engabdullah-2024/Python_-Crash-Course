# Solution to Exercise 2: Custom Money dunder methods


class Money:
    def __init__(self, dollars, cents=0):
        self.total_cents = dollars * 100 + cents

    def __repr__(self):
        d, c = divmod(self.total_cents, 100)
        return f"Money({d}, {c})"

    def __str__(self):
        d, c = divmod(self.total_cents, 100)
        return f"${d}.{c:02d}"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.total_cents == other.total_cents

    def __add__(self, other):
        return Money(0, self.total_cents + other.total_cents)


if __name__ == "__main__":
    price = Money(19, 99)
    tax = Money(1, 60)
    total = price + tax

    print(repr(price))   # Money(19, 99)
    print(price)          # $19.99
    print(total)           # $21.59
    print(price == Money(19, 99))  # True
