"""
Demonstrates a race condition on shared state, and how threading.Lock fixes it.

Run: python 04_race_condition_and_lock.py

Note: the "unsafe" result is not guaranteed to be wrong every run -- that is
the nature of race conditions. Run it a few times if it happens to come out
correct once.
"""
import threading

ITERATIONS_PER_THREAD = 100_000
NUM_THREADS = 4


def unsafe_increment(counter: dict) -> None:
    for _ in range(ITERATIONS_PER_THREAD):
        counter["value"] += 1  # read-modify-write: NOT atomic


def safe_increment(counter: dict, lock: threading.Lock) -> None:
    for _ in range(ITERATIONS_PER_THREAD):
        with lock:
            counter["value"] += 1


def run_unsafe() -> int:
    counter = {"value": 0}
    threads = [
        threading.Thread(target=unsafe_increment, args=(counter,))
        for _ in range(NUM_THREADS)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return counter["value"]


def run_safe() -> int:
    counter = {"value": 0}
    lock = threading.Lock()
    threads = [
        threading.Thread(target=safe_increment, args=(counter, lock))
        for _ in range(NUM_THREADS)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return counter["value"]


if __name__ == "__main__":
    expected = ITERATIONS_PER_THREAD * NUM_THREADS

    unsafe_result = run_unsafe()
    print(f"Expected: {expected}")
    print(f"Unsafe (no lock) result:   {unsafe_result} "
          f"{'-- lost updates!' if unsafe_result != expected else '(got lucky this run)'}")

    safe_result = run_safe()
    print(f"Safe   (with lock) result: {safe_result} "
          f"{'-- correct.' if safe_result == expected else '-- unexpected!'}")
