# Lesson 01: Syntax & Variables

Every language has grammar rules; Python's are unusually clean, and this lesson covers the ones you'll use in literally every program you write from here on: how Python groups code using indentation instead of curly braces, what a statement is, how to store data in variables, the rules and conventions for naming them, and how to inspect what "kind" of data you're holding with `type()`. Get comfortable with these basics — they're the alphabet the rest of the course is written in.

## Key Concepts

- Statements — a single instruction Python executes
- Indentation-based blocks (no `{}`, no `end`)
- Variables and assignment (`=`)
- Naming rules and `snake_case` convention
- Dynamic typing — variables don't have a fixed type
- Comments (`#`)
- The `type()` builtin

## Explanation

### Statements

A **statement** is one instruction. In Python, statements are usually one per line — there's no semicolon required at the end (unlike languages like C, Java, or JavaScript):

```python
print("Line one")
print("Line two")
```

Each line above is a complete statement, executed in order, top to bottom.

### Indentation-based blocks

Many languages group related statements ("blocks") with `{ }`. Python instead uses **indentation** — consistent leading whitespace — to mark a block. You'll see this properly with `if` statements and loops in later lessons, but here's a preview:

```python
age = 20

if age >= 18:
    print("You are an adult.")   # indented 4 spaces — part of the if-block
    print("You can vote.")       # also part of the if-block
print("This always runs.")       # not indented — outside the if-block
```

The convention (and the official style guide, PEP 8) is **4 spaces** per indentation level. Never mix tabs and spaces — Python will raise an error if a file does. Most editors (including VS Code with the Python extension) automatically insert 4 spaces when you press Tab in a `.py` file.

Indentation isn't just a style choice in Python — it's syntax. Inconsistent indentation causes an `IndentationError`.

### Variables and assignment

A **variable** is a name that refers to a value stored in memory. You create one with `=`, the **assignment operator**:

```python
name = "Ada"
age = 36
is_learning = True
```

Read `name = "Ada"` as "the name `name` now refers to the value `"Ada"`", not as mathematical equality. Once assigned, you use the variable by writing its name:

```python
print(name)          # Ada
print(name, age)     # Ada 36
```

You can reassign a variable at any time, even to a value of a different type:

```python
score = 10
print(score)   # 10
score = 20
print(score)   # 20
score = "twenty"
print(score)   # twenty
```

### Naming rules and conventions

**Rules** (Python will refuse to run your code if you break these):

- Names can contain letters, digits, and underscores (`_`).
- Names cannot start with a digit (`2cool` is invalid, `cool2` is fine).
- Names cannot be a Python keyword (`if`, `for`, `class`, `True`, etc.).
- Names are case-sensitive: `age` and `Age` are different variables.

**Conventions** (Python will run your code, but the community strongly expects these):

- Use `snake_case` for variable names: lowercase words separated by underscores, e.g. `first_name`, `total_score`, `is_valid`.
- Choose descriptive names. `n` tells the reader nothing; `num_items` does.
- Constants (values that shouldn't change) are written in `ALL_CAPS_WITH_UNDERSCORES` by convention, e.g. `MAX_SPEED = 120`. Python doesn't actually enforce immutability here — it's a signal to other programmers.

```python
# good
user_name = "Ada"
total_price = 49.99

# avoid — not descriptive, not snake_case
x = "Ada"
TotalPrice = 49.99
```

### Dynamic typing

Python is **dynamically typed**: a variable itself has no fixed type — the type belongs to the *value* it currently holds, and that can change with each reassignment (as shown above with `score`). This is different from languages like Java or C, where you must declare a variable's type up front and it can never change.

This gives flexibility but also means you should be deliberate: reassigning a variable to an unrelated type midway through a program often makes code confusing, even though Python allows it.

### Comments

A **comment** is text the Python interpreter ignores — it exists purely for humans reading the code. Anything after a `#` on a line is a comment:

```python
# This is a full-line comment explaining the next statement.
age = 30  # This is an inline comment explaining this specific line.
```

Use comments to explain *why* something is done, not to restate the obvious (`x = x + 1  # add one to x` adds no value).

### The `type()` builtin

`type()` tells you the type of a value or variable — useful for understanding what you're working with, especially while learning:

```python
print(type(30))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>

name = "Ada"
print(type(name))        # <class 'str'>
```

We'll explore each of these types (`int`, `float`, `str`, `bool`) in depth in the next lesson.

## Common Pitfalls

- **Mixing tabs and spaces.** Stick to spaces (4 per level); configure your editor to insert spaces when you press Tab.
- **Inconsistent indentation within the same block** — Python requires all statements in a block to be indented by the exact same amount, or it raises an `IndentationError`.
- **Using `=` when you mean comparison.** `=` assigns; equality comparison is `==` (covered in the next lesson). `if age = 18:` is a syntax error in Python — it forces you to write `if age == 18:`.
- **Non-descriptive variable names** like `a`, `tmp`, `data2` — they compile fine but make code hard to read and maintain.
- **Forgetting variables are case-sensitive** — `Total` and `total` are two different variables, a common source of `NameError`.

## Summary

- Python statements are usually one per line, with no semicolons required.
- Blocks are defined by indentation (4 spaces is standard) — this is enforced syntax, not just style.
- `=` assigns a value to a variable name; the variable can be reassigned to any type at any time (dynamic typing).
- Use descriptive `snake_case` names for variables; `ALL_CAPS` for constants by convention.
- `#` starts a comment; `type()` reveals the type of any value.

## Next

[Next: 02 - Data Types & Operators →](../02-data-types-and-operators/)
