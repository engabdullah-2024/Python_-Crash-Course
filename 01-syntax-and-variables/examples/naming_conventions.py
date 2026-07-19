# Demonstrates good vs. bad variable naming, and constant conventions.

# Good: descriptive snake_case names
first_name = "Grace"
last_name = "Hopper"
total_price = 49.99

# Constant by convention (Python does not truly enforce this, but ALL_CAPS
# signals to other developers "please don't reassign this")
MAX_LOGIN_ATTEMPTS = 3

print(first_name, last_name)
print("Total price:", total_price)
print("Max login attempts allowed:", MAX_LOGIN_ATTEMPTS)

# Comments explain WHY, not WHAT
attempts_left = MAX_LOGIN_ATTEMPTS - 1  # user just failed one login attempt
print("Attempts left:", attempts_left)
