# Demonstrates comparison operators and logical operators (and, or, not).

age = 25
has_id = True

print(age == 25)               # True
print(age != 30)               # True
print(age >= 18 and has_id)    # True -- both sides true
print(age < 18 or has_id)      # True -- at least one side true
print(not has_id)              # False

# Operator precedence: comparisons happen before 'and'/'or'
print(5 > 3 and 2 < 4)         # True and True -> True

# Precedence with arithmetic and parentheses
result_a = 2 + 3 * 4       # multiplication first -> 14
result_b = (2 + 3) * 4     # parentheses force addition first -> 20
print("result_a =", result_a)
print("result_b =", result_b)
