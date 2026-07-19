# Demonstrates the type() builtin and Python's dynamic typing.

value = 30
print(value, "->", type(value))

value = 3.14
print(value, "->", type(value))

value = "hello"
print(value, "->", type(value))

value = True
print(value, "->", type(value))

# The SAME variable name held four different types above -- that's dynamic typing.
