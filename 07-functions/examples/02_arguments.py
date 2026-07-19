# Default arguments, keyword arguments, *args, and **kwargs.


def power(base, exponent=2):
    """Raise base to exponent, defaulting exponent to 2 (square)."""
    return base ** exponent


def describe_pet(name, species, age):
    """Print a one-line description of a pet."""
    print(f"{name} is a {age}-year-old {species}.")


def total(*numbers):
    """Sum any number of positional arguments."""
    return sum(numbers)


def build_profile(**details):
    """Collect arbitrary keyword arguments into a dict."""
    return details


def report(title, *values, unit="items", **extra):
    """Demonstrate combining regular, *args, keyword-only, and **kwargs params."""
    print(f"{title}: {values} ({unit})")
    if extra:
        print("extra info:", extra)


if __name__ == "__main__":
    print(power(5))          # uses default exponent
    print(power(5, 3))       # overrides default

    describe_pet("Rex", "dog", 4)                  # positional
    describe_pet(name="Rex", species="dog", age=4)  # keyword
    describe_pet("Rex", age=4, species="dog")       # mixed

    print(total(1, 2, 3))
    print(total(10, 20, 30, 40))

    print(build_profile(name="Sam", role="engineer"))

    report("Sales", 10, 20, 30, unit="dollars", region="EU")
