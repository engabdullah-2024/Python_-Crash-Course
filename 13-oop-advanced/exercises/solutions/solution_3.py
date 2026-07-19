# Solution to Exercise 3: @property validated Temperature


class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @property
    def kelvin(self):
        return self._celsius + 273.15


if __name__ == "__main__":
    t = Temperature(25)
    print(t.celsius, t.fahrenheit, t.kelvin)

    t.celsius = 100
    print(t.celsius, t.fahrenheit, t.kelvin)

    try:
        t.celsius = -300
    except ValueError as e:
        print(f"Correctly rejected: {e}")
