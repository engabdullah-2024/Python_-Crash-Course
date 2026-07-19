"""
Exercise 5 (Easy): Choose the Right Tool

For each workload description below, decide which concurrency model fits
best: "threading", "multiprocessing", or "asyncio". Fill in your answers
in `choose_tool`, along with a one-sentence justification.

TODO: fill in the ANSWERS dict with your choices and reasoning. Each value
should be a tuple: (tool_name, justification).

Workloads:
  1. Downloading 5 files from different URLs.
  2. Computing the SHA-256 hash of 10 very large files (CPU-heavy).
  3. Handling 10,000 simultaneous open WebSocket connections on a server.
  4. Resizing 20 large images (CPU-heavy) on a 4-core machine.
  5. Polling 3 slow internal APIs every second and combining their results.
"""

WORKLOADS = {
    1: "Downloading 5 files from different URLs.",
    2: "Computing the SHA-256 hash of 10 very large files (CPU-heavy).",
    3: "Handling 10,000 simultaneous open WebSocket connections on a server.",
    4: "Resizing 20 large images (CPU-heavy) on a 4-core machine.",
    5: "Polling 3 slow internal APIs every second and combining their results.",
}

# TODO: replace the placeholder tuples below with your real answers.
ANSWERS = {
    1: ("TODO", "TODO: why?"),
    2: ("TODO", "TODO: why?"),
    3: ("TODO", "TODO: why?"),
    4: ("TODO", "TODO: why?"),
    5: ("TODO", "TODO: why?"),
}


def choose_tool(workload_id: int) -> tuple[str, str]:
    """Return (tool_name, justification) for the given workload id."""
    return ANSWERS[workload_id]


def main() -> None:
    for workload_id, description in WORKLOADS.items():
        tool, reason = choose_tool(workload_id)
        print(f"{workload_id}. {description}\n   -> {tool}: {reason}\n")


if __name__ == "__main__":
    main()
