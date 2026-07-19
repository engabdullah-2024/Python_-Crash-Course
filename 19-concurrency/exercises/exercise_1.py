"""
Exercise 1 (Easy): Threaded Downloader

Simulate "downloading" a list of items concurrently using
concurrent.futures.ThreadPoolExecutor.

TODO:
1. Implement `simulate_download` so it sleeps for `delay` seconds and
   returns a string like "downloaded item-3".
2. Implement `download_all_concurrent` to download all items using a
   ThreadPoolExecutor with `max_workers` workers, returning a list of
   results in the same order as `items`.
3. Implement `download_all_serial` to download all items one at a time
   (no threading) for comparison.
4. In `main`, time both approaches and print the results and timings.
   The concurrent version should be noticeably faster.
"""
import time
from concurrent.futures import ThreadPoolExecutor


def simulate_download(item: str, delay: float = 0.3) -> str:
    """TODO: sleep for `delay` seconds, then return f"downloaded {item}"."""
    # Placeholder so the file runs before you implement this.
    return f"TODO: {item}"


def download_all_concurrent(items: list[str], max_workers: int = 4) -> list[str]:
    """TODO: use ThreadPoolExecutor to download all items concurrently."""
    # Placeholder: replace with a ThreadPoolExecutor-based implementation.
    return [simulate_download(item) for item in items]


def download_all_serial(items: list[str]) -> list[str]:
    """TODO: download all items one at a time, without threading."""
    return [simulate_download(item) for item in items]


def main() -> None:
    items = [f"item-{i}" for i in range(8)]

    start = time.perf_counter()
    serial_results = download_all_serial(items)
    serial_time = time.perf_counter() - start

    start = time.perf_counter()
    concurrent_results = download_all_concurrent(items)
    concurrent_time = time.perf_counter() - start

    print(f"Serial:     {serial_time:.2f}s -> {serial_results}")
    print(f"Concurrent: {concurrent_time:.2f}s -> {concurrent_results}")


if __name__ == "__main__":
    main()
