# Lesson 02: Data Types & Operators

Now that you know how to create variables, it's time to work with the values inside them. This lesson covers Python's core built-in data types — numbers, booleans, and a first look at strings — plus the operators you use to combine and compare them: arithmetic, comparison, and logical operators, how Python decides which operator runs first, type conversion between types, and the concept of "truthiness". These are the building blocks for every calculation and decision your programs will make.

## Key Concepts

- Core types: `int`, `float`, `bool`, `str` (brief intro)
- Type conversion (`int()`, `float()`, `str()`, `bool()`)
- Arithmetic operators: `+ - * / // % **`
- Comparison operators: `== != < > <= >=`
- Logical operators: `and`, `or`, `not`
- Operator precedence
- Truthiness

## Explanation

### The core types

```python
whole_number = 42          # int   -- whole numbers, positive or negative
decimal_number = 3.14      # float -- numbers with a decimal point
flag = True                # bool  -- True or False
text = "Hello"              # str   -- text (full lesson coming in 03-strings)

print(type(whole_number))  # <class 'int'>
print(type(decimal_number))# <class 'float'>
print(type(flag))          # <class 'bool'>
print(type(text))          # <class 'str'>
```

- `int` — whole numbers with no size limit in Python (`10`, `-3`, `1_000_000`).
- `float` — numbers with a fractional part (`3.14`, `-0.5`, `2.0`). Note `2.0` is a float even though it looks whole.
- `bool` — exactly two values, `True` and `False` (capitalized). Booleans are actually a subtype of `int`: `True` behaves like `1`, `False` like `0`.
- `str` — text, wrapped in quotes. We dedicate all of Lesson 03 to strings; here we just need to know they exist.

### Type conversion

You can convert a value from one type to another using the type's name as a function:

```python
age_text = "25"
age_number = int(age_text)        # "25" -> 25
print(age_number + 1)             # 26

price = float("9.99")             # "9.99" -> 9.99
count_as_text = str(42)           # 42 -> "42"
whole = int(9.8)                  # 9.8 -> 9  (truncates, does NOT round)

print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("hi"))    # True
```

Converting an invalid string raises an error:

```python
int("hello")   # ValueError: invalid literal for int() with base 10: 'hello'
```

`int()` on a float truncates toward zero — it does not round. Use `round()` if you want rounding: `round(9.8)` gives `10`.

### Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | addition | `5 + 3` | `8` |
| `-` | subtraction | `5 - 3` | `2` |
| `*` | multiplication | `5 * 3` | `15` |
| `/` | true division | `7 / 2` | `3.5` |
| `//` | floor division | `7 // 2` | `3` |
| `%` | modulo (remainder) | `7 % 2` | `1` |
| `**` | exponent | `2 ** 3` | `8` |

```python
print(7 / 2)    # 3.5  -- "/" always returns a float
print(7 // 2)   # 3    -- floor division drops the remainder
print(7 % 2)    # 1    -- what's left over after floor division
print(2 ** 10)  # 1024 -- exponentiation
```

`%` is extremely useful for checking things like "is this number even?" (`n % 2 == 0`).

### Comparison operators

Comparisons produce a `bool`:

```python
print(5 == 5)   # True  -- equality
print(5 != 3)   # True  -- inequality
print(5 > 3)    # True
print(5 < 3)    # False
print(5 >= 5)   # True
print(5 <= 4)   # False
```

Remember: `=` assigns, `==` compares. Mixing these up is one of the most common beginner mistakes.

### Logical operators

`and`, `or`, and `not` combine or invert boolean values:

```python
age = 25
has_id = True

print(age >= 18 and has_id)     # True  -- both must be True
print(age < 18 or has_id)       # True  -- at least one must be True
print(not has_id)               # False -- inverts the value
```

- `and` — `True` only if both sides are `True`.
- `or` — `True` if at least one side is `True`.
- `not` — flips `True` to `False` and vice versa.

### Operator precedence

When an expression has multiple operators, Python evaluates them in a fixed order (highest precedence first), similar to math class "order of operations":

1. `()` parentheses (evaluated first, use to force an order)
2. `**` exponent
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. comparisons (`==`, `!=`, `<`, `>`, `<=`, `>=`)
6. `not`
7. `and`
8. `or`

```python
result = 2 + 3 * 4        # 3*4 first -> 2 + 12 = 14
print(result)

result = (2 + 3) * 4      # parentheses force + first -> 5*4 = 20
print(result)

print(5 > 3 and 2 < 4)    # comparisons first: True and True -> True
```

When in doubt, add parentheses — they cost nothing and make intent explicit for the next reader (often future you).

### Truthiness

Every value in Python can be used in a boolean context (like an `if`), and Python decides whether it counts as `True` or `False`. This is called **truthiness**. As a rule of thumb, "empty" or "zero-like" values are falsy, everything else is truthy:

```python
print(bool(0))        # False
print(bool(1))        # True
print(bool(-5))       # True  -- any nonzero number is truthy
print(bool(""))       # False -- empty string
print(bool("no"))     # True  -- any nonempty string
print(bool(None))     # False
```

We'll use truthiness constantly once we reach `if` statements and loops in Lesson 06.

## Common Pitfalls

- **Confusing `/` and `//`.** `/` always gives a float (`7 / 2 == 3.5`); `//` floors the result to an int-like value (`7 // 2 == 3`).
- **Confusing `=` (assignment) with `==` (comparison).** `if x = 5:` is a syntax error in Python — it forces you to write `if x == 5:`.
- **Assuming `int()` rounds.** It truncates toward zero: `int(9.9)` is `9`, not `10`. Use `round()` for rounding.
- **Forgetting `and`/`or` short-circuit and return one of the operands, not always a plain `True`/`False`.** For example `"" or "default"` evaluates to `"default"` — useful, but surprising if unexpected.
- **Trying to convert an incompatible string.** `int("3.14")` fails with a `ValueError` — you must go through `float()` first: `int(float("3.14"))`.

## Summary

- Python's core scalar types are `int`, `float`, `bool`, and `str`; convert between them with `int()`, `float()`, `str()`, `bool()`.
- Arithmetic operators include the beginner-tricky pair `/` (true division, always float) and `//` (floor division).
- Comparisons (`==`, `!=`, `<`, `>`, `<=`, `>=`) always produce a `bool`.
- `and`, `or`, `not` combine booleans; precedence rules decide evaluation order — use parentheses to be explicit.
- Every value has a truthiness; empty/zero-like values are falsy, everything else is truthy.

## Next

[Next: 03 - Strings →](../03-strings/)
