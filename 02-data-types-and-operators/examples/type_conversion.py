# Demonstrates converting between int, float, str, and bool.

age_text = "25"
age_number = int(age_text)
print("age_number + 1 =", age_number + 1)

price = float("9.99")
print("price =", price)

count_as_text = str(42)
print("count_as_text is", type(count_as_text), "with value", count_as_text)

whole = int(9.8)         # truncates, does not round
rounded = round(9.8)     # rounds properly
print("int(9.8) =", whole)
print("round(9.8) =", rounded)

print(bool(0), bool(1), bool(""), bool("hi"))
