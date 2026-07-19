# Exercises: Functions

Work through these in order. Each starter file has a docstring explaining the task and `TODO` markers showing where to write code. Run a file directly to check your own output, e.g.:

```
python exercise_1.py
```

Solutions are in `solutions/`, but try each exercise yourself first.

## Exercise 1: Temperature Converter (Easy)

Write a function `celsius_to_fahrenheit(celsius)` that converts a Celsius temperature to Fahrenheit and returns the result. Formula: `F = C * 9/5 + 32`.

## Exercise 2: Flexible Greeter (Easy)

Write a function `greet(name, greeting="Hello", punctuation="!")` that returns a greeting string built from its three parameters, using default arguments. Call it three different ways: with only `name`, with `name` and `greeting`, and with all three as keyword arguments.

## Exercise 3: Average Calculator with `*args` (Medium)

Write a function `average(*numbers)` that returns the average of any number of arguments passed to it. Handle the case where no arguments are passed by returning `0` instead of raising a division-by-zero error.

## Exercise 4: Profile Builder with `**kwargs` (Medium)

Write a function `build_profile(first, last, **extra_info)` that returns a dictionary containing `"first_name"`, `"last_name"`, and any additional keyword arguments merged in as-is.

## Exercise 5: Scope and a Running Total (Hard)

Write a module-level variable `running_total = 0` and a function `add_to_total(amount)` that uses the `global` keyword to add `amount` to `running_total`. Then write a second function `reset_total()` that resets `running_total` back to `0`, also using `global`. Demonstrate calling both functions and printing the result at each step.
