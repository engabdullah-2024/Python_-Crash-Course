"""
Exercise 3 (Medium): Concurrent Fetch Simulation with asyncio

Simulate fetching data for several IDs concurrently using asyncio.

TODO:
1. Implement `fetch_data` as an async function: it should print that it
   started, `await asyncio.sleep(delay)`, then return a dict like
   {"id": item_id, "data": f"payload-{item_id}"}.
2. Implement `fetch_all` to fetch a list of IDs CONCURRENTLY using
   asyncio.gather (not one at a time in a loop with individual awaits).
3. In `main` (already async), time `fetch_all` and print the total
   elapsed time -- it should be close to the single longest delay, not
   the sum of all delays.
"""
import asyncio
import time


async def fetch_data(item_id: int, delay: float) -> dict:
    """TODO: simulate an async fetch. Currently returns immediately."""
    # Placeholder -- doesn't actually await anything yet.
    return {"id": item_id, "data": f"TODO-{item_id}"}


async def fetch_all(ids_with_delays: list[tuple[int, float]]) -> list[dict]:
    """TODO: fetch all items CONCURRENTLY using asyncio.gather."""
    # Placeholder: fetches sequentially for now.
    results = []
    for item_id, delay in ids_with_delays:
        results.append(await fetch_data(item_id, delay))
    return results


async def main() -> None:
    ids_with_delays = [(1, 1.0), (2, 0.5), (3, 0.8), (4, 0.3)]

    start = time.perf_counter()
    results = await fetch_all(ids_with_delays)
    elapsed = time.perf_counter() - start

    print(f"Results: {results}")
    print(f"Elapsed: {elapsed:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
