# Python in Shell - Video Notes
**Channel:** Chai aur Code  
**Instructor:** Hitesh Choudhary  
**Video Link:** [Python in shell](https://www.youtube.com/watch?v=OEKrDogH5ew)

---

## 1. Accessing the Python Shell [00:15]
The Python Shell, also known as the **REPL** (Read-Eval-Print Loop) or **Interactive Mode**, is designed for quick testing and code interaction.

* **How to start:** Open your terminal or command prompt and type `python` or `python3`. [00:30]
* **Windows:** Users can also utilize the IDLE environment.
* **How to exit:** * **Windows:** `Ctrl + Z` then Enter.
    * **Mac/Linux:** `Ctrl + D`. [02:08]

---

## 2. Basic Operations & Immediate Execution [04:04]
The shell executes code line-by-line, providing instant feedback.

* **Printing:** Running `print("chai")` displays the output immediately. [04:34]
* **Math:** You can use it as a calculator (e.g., `2 * 2` or `3 + 5`). [05:05]
* **String Manipulation:** Python allows unique operations like `"chai" * 4`, which outputs `chaichaichaichai`. This is excellent for testing logic before committing it to a script. [05:43]

---

## 3. Variables and Error Handling [06:04]
Variables defined in the shell are stored in memory for the duration of the session.

* **Assignment:** `score = 100` stores the value.
* **NameError:** If you attempt to access an undefined variable (e.g., calling `tea` when it hasn't been assigned), Python throws a `NameError: name 'tea' is not defined`. [07:04]

---

## 4. Importing Standard Modules [07:29]
Python includes a vast library of built-in modules that can be explored directly in the shell.

* **os module:** Use `import os` and `os.getcwd()` to find your Current Working Directory. [09:04]
* **sys module:** Use `import sys` and `sys.platform` to check the operating system (e.g., `'darwin'` for Mac, `'win32'`). [11:50]
* **Syntax Tip:** Functions require parentheses `()`, while properties/attributes do not. [12:19]

---

## 5. Loops and Indentation [09:29]
Writing multi-line code in the shell requires attention to spacing.

* **IndentationError:** If you forget to add a tab or space after a colon (`:`), Python throws an error. [10:40]
* **Multi-line Input:** The "triple dots" (`...`) indicate Python is waiting for the rest of the block (like the body of a loop). Pressing **Enter on an empty line** signals the end of the block and executes it. [11:22]

---

## 6. Custom Imports & The Reloading Problem [12:38]
You can import your own `.py` files (e.g., `import hello_chai`).

* **The Issue:** If you modify your file (e.g., adding `chai_one = "lemon tea"`) while the shell is open, the shell will **not** automatically see those changes. [16:16]
* **AttributeError:** Trying to access new variables from an already imported module results in an `AttributeError` because the old version is cached in memory. [16:21]

---

## 7. How to Reload a Module (importlib) [17:12]
Instead of closing and restarting the shell, use the `importlib` library to refresh your code.

1.  `from importlib import reload`
2.  `reload(hello_chai)`

After reloading, the new variables and functions become accessible without losing the current shell state. [18:09]

---

## 8. Summary & Next Steps [18:54]
The shell is a fundamental tool for building confidence and testing snippets of logic.

* **Status:** This concludes the "Foundation" segment of the series.
* **Upcoming Topics:** Moving deeper into language specifics: Variables, Objects, Strings, Numbers, and Complex Data Types. [19:37]