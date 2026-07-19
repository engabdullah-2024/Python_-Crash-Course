"""Solution 5: Scope and a Running Total"""

running_total = 0


def add_to_total(amount):
    global running_total
    running_total += amount


def reset_total():
    global running_total
    running_total = 0


if __name__ == "__main__":
    add_to_total(10)
    print(running_total)  # 10
    add_to_total(5)
    print(running_total)  # 15
    add_to_total(-3)
    print(running_total)  # 12

    reset_total()
    print(running_total)  # 0
