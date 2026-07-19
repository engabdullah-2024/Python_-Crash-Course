"""
Exercise 3 (Medium): @property validated Temperature

Create a `Temperature` class that stores degrees internally in Celsius
as `self._celsius`, and exposes:
  - a `celsius` property (getter returns self._celsius)
  - a `celsius` setter that raises ValueError if the value is below -273.15
  - a read-only `fahrenheit` property computed from celsius:
        fahrenheit = celsius * 9 / 5 + 32
  - a read-only `kelvin` property computed from celsius:
        kelvin = celsius + 273.15
"""


class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius  # bypasses the setter's validation on purpose;
        # feel free to change this to use the setter once you've written it

    # TODO: add the `celsius` property (getter + setter)

    # TODO: add the read-only `fahrenheit` property

    # TODO: add the read-only `kelvin` property


if __name__ == "__main__":
    t = Temperature(25)
    print(t.celsius, t.fahrenheit, t.kelvin)

    t.celsius = 100
    print(t.celsius, t.fahrenheit, t.kelvin)

    try:
        t.celsius = -300
    except ValueError as e:
        print(f"Correctly rejected: {e}")
