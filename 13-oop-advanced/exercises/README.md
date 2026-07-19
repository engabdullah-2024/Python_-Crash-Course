# Exercises: OOP Advanced

Work through these in order. Each starter file has a docstring describing the
task and `TODO` markers for what to fill in. Run a file directly to check
your work (`python exercise_1.py`); each includes a small self-test at the
bottom.

1. **`exercise_1.py` — Shape hierarchy (Easy)**
   Build a small inheritance hierarchy (`Shape` -> `Rectangle`, `Circle`) with
   overridden `area()` methods and a `describe()` method that uses `super()`.

2. **`exercise_2.py` — Custom `Money` dunder methods (Medium)**
   Implement `__repr__`, `__str__`, `__eq__`, and `__add__` for a `Money`
   class so it prints nicely, compares correctly, and can be summed.

3. **`exercise_3.py` — `@property` validated `Temperature` (Medium)**
   Add a `celsius` property with a setter that validates the value, and a
   read-only `fahrenheit` computed property.

4. **`exercise_4.py` — Alternative constructors (Medium)**
   Add `@classmethod` constructors to a `Rectangle` class (`square`,
   `from_diagonal`) and a `@staticmethod` validator.

5. **`exercise_5.py` — Abstract `Notifier` interface (Hard)**
   Define an abstract base class `Notifier` with an abstract `send()` method,
   then implement two concrete notifiers and a `NotificationCenter` that uses
   composition to hold a list of notifiers.

## Difficulty guide

- Easy: applies one concept directly, similar to the lesson examples.
- Medium: combines two or three concepts, or requires a bit of your own
  design.
- Hard: requires connecting multiple concepts from the lesson to a slightly
  more open-ended design.
