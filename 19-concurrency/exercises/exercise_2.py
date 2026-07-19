"""
Exercise 2 (Medium): Parallel Sum of Squares

Use multiprocessing.Pool to compute the sum of squares of a large list of
numbers in parallel, and compare the timing against a plain serial version.

TODO:
1. Implement `square` (a plain function -- required so it can be pickled
   and sent to worker processes).
2. Implement `sum_of_squares_serial` using a simple loop or sum(map(...)).
3. Implement `sum_of_squares_parallel` using multiprocessing.Pool.map to
   distribute the squaring across `processes` worker processes, then sum
   the results.
4. In `main`, time both versions on the same input and print the results.
   Remember the `if __name__ == "__main__":` guard is required for
   multiprocessing to work correctly.
"""
import time
from multiprocessing import Pool


def square(n: int) -> int:
    """TODO: return n squared."""
    return n  # placeholder -- not actually squaring yet


def sum_of_squares_serial(numbers: list[int]) -> int:
    """TODO: compute sum of squares without multiprocessing."""
    return sum(square(n) for n in numbers)


def sum_of_squares_parallel(numbers: list[int], processes: int = 4) -> int:
    """TODO: compute sum of squares using multiprocessing.Pool.map."""
    # Placeholder: currently just calls the serial version.
    return sum_of_squares_serial(numbers)


def main() -> None:
    numbers = list(range(1, 2_000_000))

    start = time.perf_counter()
    serial_result = sum_of_squares_serial(numbers)
    serial_time = time.perf_counter() - start
    print(f"Serial:   result={serial_result} time={serial_time:.2f}s")

    start = time.perf_counter()
    parallel_result = sum_of_squares_parallel(numbers)
    parallel_time = time.perf_counter() - start
    print(f"Parallel: result={parallel_result} time={parallel_time:.2f}s")


if __name__ == "__main__":
    main()
