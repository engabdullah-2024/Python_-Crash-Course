# Lesson 00: Getting Started

This lesson gets Python installed on your machine, introduces the two ways you'll run Python code (the interactive REPL and `.py` script files), and walks you through writing and running your very first program. Everything after this lesson assumes you have a working Python installation and know how to open a terminal, so take your time here — a solid setup makes every later lesson smoother.

## Key Concepts

- What Python is and why it's a good first language
- Installing Python on Windows, macOS, and Linux
- The REPL (Read-Eval-Print Loop) — Python's interactive shell
- Running a `.py` script from a terminal
- Choosing a code editor (VS Code)
- The `print()` function
- Writing and running your first script

## Explanation

### What is Python?

Python is a general-purpose programming language known for readable syntax and a huge ecosystem of libraries. It's used for web development, data analysis, automation, machine learning, and more. You write Python code as plain text in files ending in `.py`, and the Python **interpreter** reads that text and executes it.

### Installing Python

You need Python 3.11 or newer for this course.

**Windows**

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python 3 installer.
2. Run the installer. On the first screen, **check the box "Add python.exe to PATH"** — this is the single most common source of beginner problems if skipped.
3. Click "Install Now".
4. Open a terminal (Command Prompt, PowerShell, or Windows Terminal) and verify:

```
python --version
```

You should see something like `Python 3.12.4`.

**macOS**

1. macOS ships with an old or no Python 3 by default, so install a fresh one. The easiest route is [python.org/downloads](https://www.python.org/downloads/) — download the macOS installer package and run it.
2. Alternatively, if you have [Homebrew](https://brew.sh/) installed: `brew install python`.
3. Open Terminal and verify:

```
python3 --version
```

On macOS/Linux the command is usually `python3`, not `python`, because the system may also have an old Python 2 installed as `python`.

**Linux**

Most distributions already have Python 3. Check with:

```
python3 --version
```

If it's missing or too old, install it with your package manager, e.g. on Debian/Ubuntu:

```
sudo apt update
sudo apt install python3
```

### The REPL

REPL stands for **Read-Eval-Print Loop**. It's an interactive prompt where you type one line of Python at a time and immediately see the result. It's great for quick experiments.

Open a terminal and type `python` (Windows) or `python3` (macOS/Linux). You'll see something like:

```
Python 3.12.4 (main, ...) 
>>>
```

That `>>>` is the prompt. Try typing:

```python
>>> 2 + 2
4
>>> print("hello")
hello
```

Every line you enter is executed immediately. To exit the REPL, type `exit()` and press Enter, or press `Ctrl+Z` then Enter on Windows (`Ctrl+D` on macOS/Linux).

The REPL is perfect for testing a small idea, but it doesn't save your work. For anything you want to keep, you write a **script**.

### Running a `.py` script

A script is just a text file containing Python code, saved with a `.py` extension. Create a file called `hello.py` with this content:

```python
print("Hello, Python!")
```

Then, in a terminal, navigate to the folder containing the file and run:

```
python hello.py
```

(or `python3 hello.py` on macOS/Linux). You should see:

```
Hello, Python!
```

That's it — you wrote and ran your first program.

### Choosing an editor

You can write Python in any plain-text editor, but a code-aware editor makes life much easier through syntax highlighting, autocomplete, and error detection. **[Visual Studio Code](https://code.visualstudio.com/)** (VS Code) is free, cross-platform, and the most widely used editor for Python today. After installing it:

1. Install the official **Python extension** from Microsoft (search "Python" in the Extensions panel).
2. Open your project folder with `File > Open Folder`.
3. You can run the currently open file with the ▶️ "Run" button, or just use the terminal as shown above — both work identically, since VS Code's run button is really just executing `python yourfile.py` for you.

### The `print()` function

`print()` is a **function** — a named, reusable piece of code that does something when you "call" it by writing its name followed by parentheses. `print()` displays text (or other values) to the terminal. Whatever you put inside the parentheses is shown as output:

```python
print("Hello, Python!")   # prints: Hello, Python!
print(42)                 # prints: 42
print("Sum is:", 2 + 2)   # prints: Sum is: 4
```

Notice you can pass multiple items separated by commas — `print()` will display them separated by spaces.

### Your first script, expanded

```python
# my_first_script.py
# This program introduces itself and does a small calculation.

print("Hello! I am learning Python.")
print("Let's do some math.")

result = 5 * 3
print("5 * 3 =", result)
```

Run it with `python my_first_script.py`. You'll meet `result = 5 * 3` (a variable assignment) properly in the next lesson — for now, just notice that Python read the file top to bottom and executed each line in order.

## Common Pitfalls

- **Forgetting to add Python to PATH on Windows.** If `python --version` gives "not recognized", reinstall and check the "Add to PATH" box, or search for "Add Python to PATH" instructions for your version.
- **Using `python` instead of `python3` on macOS/Linux** (or vice versa). If one doesn't work, try the other.
- **Running the file from the wrong folder.** If your terminal isn't in the same directory as `hello.py`, `python hello.py` will fail with "No such file or directory". Use `cd` to navigate there first, or `cd` into the folder in your editor's terminal.
- **Confusing the REPL with a script.** Code typed into the REPL is not saved anywhere. If you want to keep it, put it in a `.py` file.
- **Forgetting the parentheses on `print`.** In Python 3, `print "hello"` (no parentheses) is a syntax error — that was Python 2 syntax. Always use `print("hello")`.

## Summary

- Python 3.11+ must be installed and available on your terminal's PATH before you can run any code in this course.
- The REPL (`python` / `python3`) is for quick, throwaway experiments; `.py` scripts are for anything you want to save and rerun.
- VS Code with the Python extension is a solid, free editor choice.
- `print()` is how your programs display output to the terminal.
- You now know the full loop: write code in a `.py` file, save it, run it with `python filename.py`.

## Next

[Next: 01 - Syntax & Variables →](../01-syntax-and-variables/)

[← Back to course overview](../README.md)
