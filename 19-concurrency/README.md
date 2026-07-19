# Lesson 19: Concurrency

Real programs often wait on things — network responses, disk reads, user input — or need to crunch numbers faster than one CPU core allows. Python gives you three different tools for this: `threading`, `multiprocessing`, and `asyncio`. They are not interchangeable, and picking the wrong one for the job is one of the most common performance mistakes intermediate Python developers make. This lesson explains what each tool is actually good for, why the Global Interpreter Lock (GIL) shapes all of these decisions, and how to avoid the classic pitfall of concurrent programming: race conditions.

## Key Concepts

- The Global Interpreter Lock (GIL) and what it does and doesn't allow
- `threading` for I/O-bound concurrency (`Thread`, `ThreadPoolExecutor`)
- `multiprocessing` for CPU-bound parallelism (`Pool`, `Process`)
- `asyncio` for cooperative, single-threaded concurrency (`async def`, `await`, `asyncio.run`)
- Choosing the right model: I/O-bound vs. CPU-bound
- Race conditions and `threading.Lock`

## Explanation

### The GIL: what it actually means

CPython (the standard Python implementation) has a Global Interpreter Lock: only one thread can execute Python bytecode at any given instant, even on a multi-core machine. This surprises people coming from languages like Java or C++.

The practical consequences:

- **Threads do not give you parallel CPU execution** in CPython. Two threads doing pure number-crunching will not run any faster than one thread — often slightly slower due to overhead.
- **Threads are still very useful for I/O-bound work.** When a thread is waiting on a network call, a disk read, or `time.sleep()`, it releases the GIL, so other threads can run. This means threads are great for "waiting", not "computing".
- **`multiprocessing` sidesteps the GIL entirely** by running separate Python processes, each with its own interpreter and memory space and its own GIL. This gives you true parallelism for CPU-bound work, at the cost of higher memory usage and slower inter-process communication.
- **`asyncio` sidesteps the GIL problem differently**: it runs everything on a single thread but switches between tasks cooperatively at `await` points, which is extremely efficient for large numbers of concurrent I/O-bound operations (think: thousands of open network connections).

Rule of thumb:

| Workload | Tool |
|---|---|
| Waiting on network/disk, small number of tasks | `threading` |
| Waiting on network/disk, thousands of tasks | `asyncio` |
| Heavy CPU computation | `multiprocessing` |

### `threading`: good for I/O-bound work

```python
import threading
import time


def download(name: str, delay: float) -> None:
    print(f"[{name}] starting")
    time.sleep(delay)  # stands in for a network call
    print(f"[{name}] done")


threads = [
    threading.Thread(target=download, args=(f"task-{i}", 1))
    for i in range(3)
]

start = time.perf_counter()
for t in threads:
    t.start()
for t in threads:
    t.join()  # wait for each thread to finish

print(f"Total time: {time.perf_counter() - start:.2f}s")
# All three 1-second "downloads" run concurrently, so this
# takes about 1 second, not 3.
```

For a pool of workers processing many tasks, `concurrent.futures.ThreadPoolExecutor` is more convenient than managing `Thread` objects by hand:

```python
from concurrent.futures import ThreadPoolExecutor
import time


def fetch(item_id: int) -> str:
    time.sleep(0.5)
    return f"result-{item_id}"


with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch, range(8)))

print(results)
```

`pool.map` runs `fetch` across the pool's worker threads and returns results in the original order, blocking until all are done.

### `multiprocessing`: good for CPU-bound work

```python
from multiprocessing import Pool
import time


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


if __name__ == "__main__":  # required on Windows / spawn start method
    numbers = list(range(100_000, 100_500))

    start = time.perf_counter()
    with Pool(processes=4) as pool:
        results = pool.map(is_prime, numbers)
    print(f"Found {sum(results)} primes in {time.perf_counter() - start:.2f}s")
```

Each worker in the `Pool` is a separate OS process with its own GIL, so this genuinely uses multiple CPU cores. The `if __name__ == "__main__":` guard is required because, on Windows and with the `spawn` start method, child processes re-import the main module — without the guard, you'd recursively spawn new pools forever.

### `asyncio`: cooperative concurrency

`asyncio` lets you write code that *looks* sequential but runs concurrently, by explicitly marking the points where a task is willing to give up control (`await`).

```python
import asyncio


async def fetch_page(name: str, delay: float) -> str:
    print(f"[{name}] requesting...")
    await asyncio.sleep(delay)  # stands in for an async network call
    print(f"[{name}] received")
    return f"<html for {name}>"


async def main() -> None:
    results = await asyncio.gather(
        fetch_page("home", 1.0),
        fetch_page("about", 0.5),
        fetch_page("contact", 0.8),
    )
    print(results)


asyncio.run(main())
```

`asyncio.gather` schedules all three coroutines to run concurrently on the single event loop. Total run time is about 1 second (the slowest one), not 2.3 seconds. This is the asyncio equivalent of the threading example above, but using one thread instead of three.

A few core rules:

- A function defined with `async def` is a **coroutine function**; calling it returns a coroutine object, it doesn't run the body yet.
- `await` can only be used inside an `async def` function, and only on "awaitable" objects (other coroutines, `asyncio.sleep`, async library calls, tasks).
- `asyncio.run(main())` is the standard entry point — it creates an event loop, runs `main()` to completion, and cleans up.
- Real async I/O libraries (e.g. `aiohttp`, `asyncpg`) release control at `await` points the same way `asyncio.sleep` does here; regular blocking calls (like `requests.get` or `time.sleep`) do **not** cooperate and will freeze the whole event loop if used inside async code.

### Race conditions and locks

When multiple threads read and modify shared state without coordination, you get **race conditions** — bugs that depend on the unpredictable timing of thread execution.

```python
import threading

counter = 0

def increment() -> None:
    global counter
    for _ in range(100_000):
        counter += 1  # NOT atomic: read, add, write — can be interrupted mid-way

threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # Frequently NOT 400,000 — the increments stomp on each other
```

`counter += 1` looks like a single operation but is really three steps (read, add, write). A thread can be paused by the OS scheduler between those steps, and another thread can read the stale value in the meantime, causing lost updates.

The fix is a `threading.Lock`, which ensures only one thread executes the protected section at a time:

```python
import threading

counter = 0
lock = threading.Lock()

def increment() -> None:
    global counter
    for _ in range(100_000):
        with lock:  # acquires on enter, releases on exit, even on exception
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # Reliably 400,000
```

`asyncio` code is far less prone to this specific class of bug because only one coroutine runs at a time on the event loop — but it is not immune. If a coroutine does multiple `await`s while touching shared state, another task can interleave in between and cause similar logical races. `asyncio.Lock` exists for exactly this situation.

## Common Pitfalls

- **Using threads for CPU-bound work and expecting a speedup.** The GIL means pure-Python number crunching does not get faster with more threads — use `multiprocessing` instead.
- **Forgetting the `if __name__ == "__main__":` guard with `multiprocessing`** on Windows, causing infinite process spawning or crashes.
- **Calling blocking functions (`time.sleep`, `requests.get`, heavy computation) inside `async def` code.** This blocks the entire event loop, defeating the purpose of asyncio. Use `await asyncio.sleep(...)` or async-native libraries instead.
- **Mutating shared state from multiple threads without a lock**, producing intermittent, hard-to-reproduce bugs that may not show up in quick tests.
- **Forgetting to `await` a coroutine.** `fetch_page("home", 1.0)` without `await` just creates a coroutine object and does nothing — Python will emit a `RuntimeWarning: coroutine was never awaited`.

## Summary

- The GIL means only `multiprocessing` gives true CPU parallelism in CPython; `threading` and `asyncio` do not speed up CPU-bound code.
- Use `threading` (or `ThreadPoolExecutor`) for a moderate number of I/O-bound tasks; use `asyncio` for a very large number of I/O-bound tasks with less overhead per task.
- Use `multiprocessing.Pool` for CPU-bound work that can be split across cores.
- Shared mutable state across threads needs a `threading.Lock` (or similar primitive) to avoid race conditions.
- `asyncio` code must consistently use non-blocking, awaitable operations — one blocking call can stall everything.

## Next

[Next: 20 - Type Hints →](../20-type-hints/)
[← Back to course overview](../README.md)
