# Python Crash Course — Beginner to Pro

A complete, self-contained Python curriculum: 24 lessons taking you from "what is a variable" to writing tested, typed, packaged, concurrent Python and shipping a capstone project.

Every lesson lives in its own numbered folder and follows the same shape:

```
NN-lesson-name/
├── README.md              # Explanation: concepts, code, pitfalls, summary
├── examples/               # Runnable scripts demonstrating the concepts
│   └── *.py
└── exercises/
    ├── README.md            # Exercise instructions & difficulty
    ├── exercise_*.py        # Starter files with TODOs (no solutions)
    └── solutions/
        └── solution_*.py    # Full worked solutions
```

Run any example or exercise with:

```bash
python 01-syntax-and-variables/examples/hello.py
```

## Prerequisites

- Python 3.11+ installed ([python.org](https://www.python.org/downloads/))
- A terminal and a text editor / IDE (VS Code recommended)
- No prior programming experience required for Part 1; later parts assume you've completed earlier lessons

Check your install:

```bash
python --version
```

## How to use this course

1. Go in order — later lessons assume earlier ones.
2. Read the lesson `README.md` first.
3. Run every file in `examples/` and actually read the output — don't just skim the code.
4. Attempt `exercises/` yourself before opening `exercises/solutions/`.
5. Each lesson should take 30–90 minutes depending on experience.

## Curriculum

### Part 1 — Foundations
| # | Lesson | Topics |
|---|--------|--------|
| 00 | [Getting Started](00-getting-started/) | Installing Python, the REPL, running scripts, choosing an editor |
| 01 | [Syntax & Variables](01-syntax-and-variables/) | Indentation, variables, naming, assignment, comments |
| 02 | [Data Types & Operators](02-data-types-and-operators/) | int/float/bool/str, arithmetic, comparison, logical operators |
| 03 | [Strings](03-strings/) | Slicing, formatting, f-strings, common string methods |
| 04 | [Lists & Tuples](04-lists-and-tuples/) | Sequences, indexing, mutability, common operations |
| 05 | [Dicts & Sets](05-dicts-and-sets/) | Hash-based collections, keys/values, set algebra |
| 06 | [Control Flow](06-control-flow/) | `if`/`elif`/`else`, `for`, `while`, `break`/`continue` |

### Part 2 — Core Python
| # | Lesson | Topics |
|---|--------|--------|
| 07 | [Functions](07-functions/) | Parameters, return values, scope, `*args`/`**kwargs`, lambdas |
| 08 | [Comprehensions](08-comprehensions/) | List/dict/set comprehensions, generator expressions |
| 09 | [Modules & Packages](09-modules-and-packages/) | `import`, packages, `__init__.py`, the module search path |
| 10 | [File I/O](10-file-io/) | Reading/writing files, `with`, paths, CSV/JSON basics |
| 11 | [Error Handling](11-error-handling/) | `try`/`except`/`finally`, custom exceptions, `raise` |
| 12 | [OOP Basics](12-oop-basics/) | Classes, objects, `__init__`, instance vs class attributes |

### Part 3 — Advanced Python
| # | Lesson | Topics |
|---|--------|--------|
| 13 | [OOP Advanced](13-oop-advanced/) | Inheritance, polymorphism, dunder methods, composition |
| 14 | [Decorators & Closures](14-decorators-and-closures/) | Closures, first-class functions, writing decorators |
| 15 | [Generators & Iterators](15-generators-and-iterators/) | The iterator protocol, `yield`, lazy evaluation |
| 16 | [Standard Library Tour](16-standard-library-tour/) | `os`, `sys`, `datetime`, `collections`, `itertools`, `json`, `re` |
| 17 | [Testing](17-testing/) | `unittest`, `pytest`, fixtures, mocking, TDD basics |
| 18 | [Virtual Envs & Packaging](18-virtual-envs-and-packaging/) | `venv`, `pip`, `requirements.txt`, `pyproject.toml` |

### Part 4 — Professional Python
| # | Lesson | Topics |
|---|--------|--------|
| 19 | [Concurrency](19-concurrency/) | `threading`, `multiprocessing`, `asyncio`, the GIL |
| 20 | [Type Hints](20-type-hints/) | Static typing, `mypy`, `typing`, generics |
| 21 | [APIs & Databases](21-apis-and-databases/) | `requests`, REST APIs, `sqlite3`, ORMs at a glance |
| 22 | [Design Patterns & Clean Code](22-design-patterns-and-clean-code/) | SOLID, common patterns, refactoring, code review habits |
| 23 | [Capstone Project](23-capstone-project/) | Build and ship a complete CLI application from scratch |

## License

MIT — use this freely for learning, teaching, or interviewing.
