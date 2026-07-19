"""
Exercise 1 (Easy): Shape hierarchy

Create:
  - a base class `Shape` with:
      - an __init__ that takes `name` and stores it
      - a method `area()` that raises NotImplementedError
      - a method `describe()` that returns f"{self.name} has area {self.area():.2f}"
  - a subclass `Rectangle(Shape)` with __init__(self, width, height) that
    calls super().__init__("Rectangle") and stores width/height, and
    overrides area() to return width * height
  - a subclass `Circle(Shape)` with __init__(self, radius) that calls
    super().__init__("Circle") and stores radius, and overrides area()
    to return 3.14159 * radius ** 2

Do NOT override describe() -- it should be inherited as-is from Shape.
"""


class Shape:
    def __init__(self, name):
        # TODO: store name
        pass

    def area(self):
        raise NotImplementedError

    def describe(self):
        # TODO: return f"{self.name} has area {self.area():.2f}"
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        # TODO
        pass

    def area(self):
        # TODO
        pass


class Circle(Shape):
    def __init__(self, radius):
        # TODO
        pass

    def area(self):
        # TODO
        pass


if __name__ == "__main__":
    shapes = [Rectangle(3, 4), Circle(2)]
    for shape in shapes:
        print(shape.describe())
