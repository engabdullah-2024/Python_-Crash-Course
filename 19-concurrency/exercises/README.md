# Lesson 19 Exercises: Concurrency

Work through these in order. Run each starter file to confirm it executes before you begin (it will run, but not do the full job yet — that's your task).

## Exercise 1: Threaded Downloader (Easy)

`exercise_1.py` — Use `ThreadPoolExecutor` to "download" a list of items concurrently (simulated with `time.sleep`). Measure and print how long it took, and show it's faster than doing them one at a time.

## Exercise 2: Parallel Sum of Squares (Medium)

`exercise_2.py` — Use `multiprocessing.Pool` to compute the sum of squares of a large list of numbers, splitting the work across processes. Compare timing against a plain serial version.

## Exercise 3: Concurrent Fetch Simulation with asyncio (Medium)

`exercise_3.py` — Write an async function that simulates fetching data for a given ID (using `asyncio.sleep` with a random-ish delay). Use `asyncio.gather` to fetch several IDs concurrently and print the total elapsed time.

## Exercise 4: Fix the Race Condition (Hard)

`exercise_4.py` — You're given a broken program where multiple threads update a shared bank balance without synchronization, causing lost updates. Fix it using `threading.Lock` so the final balance is always correct.

## Exercise 5: Choose the Right Tool (Easy)

`exercise_5.py` — A short quiz-style exercise: given several workload descriptions, fill in which concurrency model (`threading`, `multiprocessing`, or `asyncio`) is the best fit and briefly justify why, as a function returning your answers.

---

Solutions are in `solutions/`. Try each exercise yourself first — you'll learn more from getting stuck than from reading the answer.
