"""Solution to Exercise 1: Threaded Downloader."""
import time
from concurrent.futures import ThreadPoolExecutor


def simulate_download(item: str, delay: float = 0.3) -> str:
    time.sleep(delay)
    return f"downloaded {item}"


def download_all_concurrent(items: list[str], max_workers: int = 4) -> list[str]:
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        return list(pool.map(simulate_download, items))


def download_all_serial(items: list[str]) -> list[str]:
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
    assert concurrent_time < serial_time


if __name__ == "__main__":
    main()
