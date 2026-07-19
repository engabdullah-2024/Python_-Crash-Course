"""Solution 1: Temperature Converter"""


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    print(celsius_to_fahrenheit(0))    # 32.0
    print(celsius_to_fahrenheit(100))  # 212.0
    print(celsius_to_fahrenheit(37))   # 98.6
