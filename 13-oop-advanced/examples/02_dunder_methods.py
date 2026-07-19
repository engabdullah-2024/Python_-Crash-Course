# Making a custom class behave like a built-in type via dunder methods.


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5)

    def __iter__(self):
        yield self.x
        yield self.y


if __name__ == "__main__":
    a = Vector(3, 4)
    b = Vector(1, 2)

    print(a)               # (3, 4)          -> __str__
    print(repr(a))          # Vector(3, 4)    -> __repr__
    print(a == Vector(3, 4))  # True          -> __eq__
    print(a + b)            # (4, 6)          -> __add__ then __str__
    print(len(a))            # 5              -> __len__
    x, y = a                 # unpacking      -> __iter__
    print(f"unpacked: x={x}, y={y}")

    vectors = [a, b, Vector(0, 0)]
    print(sorted(vectors, key=len))  # relies on __len__ and __repr__
