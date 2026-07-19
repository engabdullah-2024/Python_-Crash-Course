# Lambda functions and treating functions as first-class objects.


def shout(text):
    return text.upper() + "!"


def whisper(text):
    return text.lower() + "..."


def greet_with(style_function, name):
    """Accepts a function as an argument and calls it."""
    print(style_function(name))


if __name__ == "__main__":
    square = lambda x: x ** 2
    print(square(5))

    words = ["banana", "kiwi", "fig", "apple"]
    words.sort(key=lambda w: len(w))
    print(words)

    greet_with(shout, "hello")
    greet_with(whisper, "hello")

    operations = {
        "shout": shout,
        "whisper": whisper,
    }
    print(operations["shout"]("hi"))

    # Functions can be stored in lists and looped over too.
    pipeline = [shout, whisper]
    for func in pipeline:
        print(func("pipeline step"))
