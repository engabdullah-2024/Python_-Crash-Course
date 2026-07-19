"""Solution 2: Flexible Greeter"""


def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


if __name__ == "__main__":
    print(greet("Amina"))
    print(greet("Amina", "Hi"))
    print(greet(name="Amina", greeting="Yo", punctuation="?"))
