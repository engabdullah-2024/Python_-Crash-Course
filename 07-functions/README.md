# Lesson 07: Functions

Functions are how you package up a piece of logic, give it a name, and reuse it without copy-pasting code. Every non-trivial Python program is built from functions calling other functions. This lesson covers how to define them, how arguments really work, how scope determines what a function can see, and how to treat functions as values in their own right — a habit that pays off heavily once you get to higher-order functions, callbacks, and decorators later in the course.

## Key Concepts

- Defining functions with `def`, and the difference between a *parameter* (the name in the definition) and an *argument* (the value passed at call time)
- Return values, and what happens when a function has no explicit `return`
- Default argument values
- Positional vs. keyword arguments
- Variable-length arguments: `*args` and `**kwargs`
- Variable scope: local vs. global, and the `global` keyword
- Docstrings as living documentation
- Lambda functions for small, throwaway logic
- Functions as first-class objects

## Explanation

### Defining a function

```python
def greet(name):
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"

message = greet("Amina")
print(message)  # Hello, Amina!
```

`name` is a **parameter**. `"Amina"` is the **argument** you passed for it. The triple-quoted string right after the `def` line is a **docstring** — it documents what the function does and shows up when someone calls `help(greet)`.

### Return values

A function returns whatever follows `return`. If there's no `return` statement, or a bare `return` with nothing after it, the function returns `None`.

```python
def log_message(msg):
    print(f"[LOG] {msg}")
    # no return statement

result = log_message("starting up")
print(result)  # None
```

This is a common source of bugs: forgetting that a function doesn't automatically hand back the last value it computed. You have to say `return` explicitly.

### Default arguments

You can give a parameter a default value, which makes it optional for the caller:

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))       # 25  (exponent defaults to 2)
print(power(5, 3))    # 125
```

**Pitfall:** never use a mutable object (like a list or dict) as a default value. Defaults are evaluated *once*, when the function is defined — not on every call — so a mutable default gets shared and mutated across calls in surprising ways. See "Common Pitfalls" below.

### Positional vs. keyword arguments

Arguments can be passed by position (order matters) or by keyword (order doesn't matter, but the name must match):

```python
def describe_pet(name, species, age):
    print(f"{name} is a {age}-year-old {species}.")

describe_pet("Rex", "dog", 4)                       # positional
describe_pet(name="Rex", species="dog", age=4)       # keyword
describe_pet("Rex", age=4, species="dog")            # mixed — positional first, then keyword
```

Once you use a keyword argument, every argument after it must also be a keyword argument. Keyword arguments make calls self-documenting, which matters a lot once a function has more than two or three parameters.

### `*args` and `**kwargs`

Sometimes you don't know in advance how many arguments a function should accept. `*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dict.

```python
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))        # 6
print(total(10, 20, 30, 40)) # 100

def build_profile(**details):
    return details

print(build_profile(name="Sam", role="engineer"))
# {'name': 'Sam', 'role': 'engineer'}
```

You can combine them all in one signature, and the order is fixed: regular positional parameters, then `*args`, then keyword-only parameters, then `**kwargs`.

```python
def report(title, *values, unit="items", **extra):
    print(f"{title}: {values} ({unit})")
    if extra:
        print("extra info:", extra)

report("Sales", 10, 20, 30, unit="dollars", region="EU")
# Sales: (10, 20, 30) (dollars)
# extra info: {'region': 'EU'}
```

The names `args` and `kwargs` are just convention — the `*` and `**` are what matter — but stick with the convention; everyone reading your code will expect it.

### Variable scope

A variable created inside a function is **local** to that function — it doesn't exist outside it, and it doesn't clash with a variable of the same name elsewhere.

```python
x = 10

def show_x():
    x = 99  # this is a *new*, local x
    print("inside:", x)

show_x()
print("outside:", x)
# inside: 99
# outside: 10
```

Functions *can* read variables from the enclosing (global) scope without any special syntax:

```python
counter = 0

def show_counter():
    print(counter)  # reading is fine

show_counter()  # 0
```

But if you try to *assign* to a global variable inside a function, Python assumes you want a local variable instead, unless you tell it otherwise with `global`:

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)  # 2
```

Use `global` sparingly. Functions that mutate global state are harder to test and reason about. Prefer passing values in and returning results out.

### Lambda functions

A `lambda` is a small, anonymous, single-expression function. It's useful when you need a quick throwaway function, often as an argument to something like `sorted()`.

```python
square = lambda x: x ** 2
print(square(5))  # 25

words = ["banana", "kiwi", "fig", "apple"]
words.sort(key=lambda w: len(w))
print(words)  # ['fig', 'kiwi', 'apple', 'banana']
```

A `lambda` can only contain a single expression (no statements, no multiple lines). If the logic is more than a one-liner, write a normal `def` function instead — it's more readable and can have a docstring.

### Functions as first-class objects

In Python, functions are values, just like integers or strings. You can assign them to variables, store them in data structures, and pass them as arguments to other functions.

```python
def shout(text):
    return text.upper() + "!"

def whisper(text):
    return text.lower() + "..."

def greet_with(style_function, name):
    print(style_function(name))

greet_with(shout, "hello")    # HELLO!
greet_with(whisper, "hello")  # hello...

# storing functions in a dict
operations = {
    "shout": shout,
    "whisper": whisper,
}
print(operations["shout"]("hi"))  # HI!
```

This is the foundation for callbacks, strategy patterns, and — later in the course — decorators.

## Common Pitfalls

- **Mutable default arguments.** `def add_item(item, bucket=[]):` reuses the *same* list across every call that doesn't pass its own `bucket`, silently accumulating items from unrelated calls. Use `None` as the default and create the mutable object inside the function instead.
- **Forgetting `return`.** A function that only `print`s never gives the caller a usable value; `result = my_func()` will just be `None`.
- **Confusing `print` with `return`.** Printing shows something to the user; returning hands a value back to the code that called the function. A function frequently needs to do the latter, not the former.
- **Overusing `global`.** It's tempting once you learn the keyword, but it makes functions depend on state outside their own arguments, which makes bugs harder to trace.
- **Cramming too much logic into a `lambda`.** If you need an `if`/`else` with several branches or more than one line, that's a sign to write a proper named function.

## Summary

- `def` creates a function; parameters are placeholders, arguments are the actual values supplied at call time.
- Use `return` to send a value back; without it, a function returns `None`.
- Default, keyword, `*args`, and `**kwargs` parameters give you flexible, self-documenting function signatures.
- Variables assigned inside a function are local by default; use `global` only when you deliberately need to modify a module-level variable.
- Functions are ordinary objects — they can be assigned, stored, and passed around like any other value.

## Next

[Next: 08 - Comprehensions →](../08-comprehensions/)
[← Back to course overview](../README.md)
