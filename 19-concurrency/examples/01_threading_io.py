"""
Demonstrates threading for I/O-bound work using both raw Thread objects
and ThreadPoolExecutor.

Run: python 01_threading_io.py
"""
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def simulate_download(name: str, delay: float) -> None:
    """Pretend to download something by sleeping (a stand-in for network I/O)."""
    print(f"[{name}] starting...")
    time.sleep(delay)
    print(f"[{name}] done.")


def demo_raw_threads() -> None:
    print("--- Raw Thread objects ---")
    threads = [
        threading.Thread(target=simulate_download, args=(f"task-{i}", 1))
        for i in range(3)
    ]

    start = time.perf_counter()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    elapsed = time.perf_counter() - start

    print(f"Ran 3 x 1s tasks concurrently in {elapsed:.2f}s (not ~3s)\n")


def fetch(item_id: int) -> str:
    time.sleep(0.3)
    return f"result-{item_id}"


def demo_thread_pool() -> None:
    print("--- ThreadPoolExecutor ---")
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, range(8)))
    elapsed = time.perf_counter() - start

    print(f"Results: {results}")
    print(f"8 x 0.3s tasks with 4 workers took {elapsed:.2f}s (not ~2.4s)\n")


if __name__ == "__main__":
    demo_raw_threads()
    demo_thread_pool()
