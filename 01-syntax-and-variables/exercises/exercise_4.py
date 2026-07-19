"""
Exercise 4 (Medium): Indentation debugging.

The code below is meant to print:
    Temperature check
    It's cold outside.
    Consider wearing a jacket.
    Done checking.

But the indentation is broken (mixed / inconsistent), which will raise
an IndentationError. Fix the indentation so it runs and matches the
expected output above.

TODO: fix the indentation below without changing the logic.
"""

temperature = 5
print("Temperature check")
if temperature < 10:
   print("It's cold outside.")
     print("Consider wearing a jacket.")
print("Done checking.")
