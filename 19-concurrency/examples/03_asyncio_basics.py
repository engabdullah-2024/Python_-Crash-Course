"""
Demonstrates asyncio basics: async def, await, asyncio.run, and running
several "fetches" concurrently with asyncio.gather.

Run: python 03_asyncio_basics.py
"""
import asyncio
import time


async def fetch_page(name: str, delay: float) -> str:
    """Simulates an async network request using asyncio.sleep.

    asyncio.sleep is non-blocking: while this coroutine is "sleeping",
    the event loop is free to run other coroutines.
    """
    print(f"[{name}] requesting...")
    await asyncio.sleep(delay)
    print(f"[{name}] received")
    return f"<html for {name}>"


async def main() -> None:
    start = time.perf_counter()

    results = await asyncio.gather(
        fetch_page("home", 1.0),
        fetch_page("about", 0.5),
        fetch_page("contact", 0.8),
    )

    elapsed = time.perf_counter() - start
    print(f"\nResults: {results}")
    print(f"Total time: {elapsed:.2f}s (about 1.0s, the slowest task -- not 2.3s)")


async def sequential_for_comparison() -> None:
    """Same three fetches, but awaited one at a time instead of concurrently."""
    start = time.perf_counter()
    await fetch_page("seq-1", 0.5)
    await fetch_page("seq-2", 0.5)
    await fetch_page("seq-3", 0.5)
    elapsed = time.perf_counter() - start
    print(f"Sequential total: {elapsed:.2f}s (about 1.5s -- each awaited in turn)")


if __name__ == "__main__":
    asyncio.run(main())
    print()
    asyncio.run(sequential_for_comparison())
