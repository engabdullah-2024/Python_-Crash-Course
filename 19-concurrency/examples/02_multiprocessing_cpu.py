"""
Demonstrates multiprocessing for CPU-bound work.

Run: python 02_multiprocessing_cpu.py

Note: the if __name__ == "__main__" guard is required for multiprocessing
to work correctly, especially on Windows.
"""
import time
from multiprocessing import Pool


def is_prime(n: int) -> bool:
    """CPU-bound check: is n a prime number?"""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def run_serial(numbers: list[int]) -> tuple[int, float]:
    start = time.perf_counter()
    count = sum(1 for n in numbers if is_prime(n))
    return count, time.perf_counter() - start


def run_parallel(numbers: list[int], processes: int = 4) -> tuple[int, float]:
    start = time.perf_counter()
    with Pool(processes=processes) as pool:
        results = pool.map(is_prime, numbers)
    return sum(results), time.perf_counter() - start


if __name__ == "__main__":
    numbers = list(range(100_000, 130_000))

    serial_count, serial_time = run_serial(numbers)
    print(f"Serial:   {serial_count} primes found in {serial_time:.2f}s")

    parallel_count, parallel_time = run_parallel(numbers)
    print(f"Parallel: {parallel_count} primes found in {parallel_time:.2f}s")

    print(
        "\nOn a multi-core machine, parallel should be noticeably faster. "
        "Threads would NOT show this speedup for CPU-bound work, because "
        "of the GIL."
    )
