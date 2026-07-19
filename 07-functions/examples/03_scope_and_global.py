# Local vs. global scope, and the `global` keyword.

x = 10
counter = 0


def show_x():
    x = 99  # this creates a *new* local x, does not touch the global one
    print("inside show_x:", x)


def show_counter():
    print("reading counter (no global needed):", counter)


def increment():
    global counter
    counter += 1


def mutable_default_pitfall(item, bucket=None):
    """Correct pattern: use None as the default, create the list inside."""
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


if __name__ == "__main__":
    show_x()
    print("outside show_x:", x)

    show_counter()
    increment()
    increment()
    print("counter after two increments:", counter)

    print(mutable_default_pitfall("first"))
    print(mutable_default_pitfall("second"))  # starts fresh, not shared
