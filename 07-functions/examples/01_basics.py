# Basic function definitions, return values, and docstrings.


def greet(name):
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def log_message(msg):
    """Print a message but return nothing (returns None)."""
    print(f"[LOG] {msg}")


if __name__ == "__main__":
    print(greet("Amina"))
    print(add(3, 4))

    result = log_message("starting up")
    print("log_message returned:", result)

    print(greet.__doc__)
