"""Solution 3: Average Calculator with *args"""


def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print(average(1, 2, 3))  # 2.0
    print(average(10, 20))   # 15.0
    print(average())         # 0
