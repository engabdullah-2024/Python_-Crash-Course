# Demonstrates Python's truthiness rules for different values.

values = [0, 1, -5, "", "no", None, 3.14, 0.0]

for value in values:
    print(f"bool({value!r}) = {bool(value)}")
