# Demonstrates all the arithmetic operators, including / vs // and %.

a = 7
b = 2

print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)    # true division -> float
print("a // b =", a // b)   # floor division -> drops remainder
print("a % b  =", a % b)    # remainder
print("a ** b =", a ** b)   # exponent

# A common use of % : checking even/odd
for n in (4, 7):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
