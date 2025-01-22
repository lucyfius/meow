
# Meow | programming language

**who knew carrs can code?????** 🐾  

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Running Your First Meow Script](#running-your-first-meow-script)
3. [Syntax and Features](#syntax-and-features)
   - [Keywords](#keywords)
   - [Operators](#operators)
   - [Comments](#comments)
   - [Examples](#examples)
4. [Advanced Features](#advanced-features)
   - [Functions](#functions)
   - [Arrays and Strings](#arrays-and-strings)
   - [File I/O](#file-io)
   - [Exception Handling](#exception-handling)
5. [Built-In Functions](#built-in-functions)
6. [Contributing](#contributing)
7. [License](#license)

---

## Introduction

Welcome to **Meow**, a language for cars, if you're not a car, do not use...  D:

---

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/meow.git
   cd meow
   ```

2. Ensure Python 3.7+ is installed on your system.

3. Run the interpreter:
   ```bash
   python meow_interpreter.py
   ```

### Running Your First Meow Script

1. Create a `.meow` script file:
   ```bash
   touch hello.meow
   ```

2. Add the following code to `hello.meow`:
   ```
   meow greeting ~= "Hello, World!"
   PURR greeting
   HISSSS()
   ```

3. Run the script:
   ```bash
   python meow_interpreter.py hello.meow
   ```

You should see:
```
😺 *purrs contentedly* Hello, World!
🙀 *dramatic cat screech* Program terminated with a HISSSS!
```

---

## Syntax and Features

### Keywords

| Keyword       | Description                              |
|---------------|------------------------------------------|
| `meow`        | Declare variables.                      |
| `PURR`        | Print a variable or value.              |
| `HISSSS`      | Terminate the program.                  |
| `meowmeow`    | Define a function.                      |
| `catnip`      | Start an `if` condition.                |
| `else`        | Start an `else` condition.              |
| `tail`        | Start a loop.                           |
| `nyaa`        | Return a value from a function.         |

### Operators

| Operator      | Description                              |
|---------------|------------------------------------------|
| `~=`          | Assignment (equals).                    |
| `>:3`         | Greater than.                           |
| `<:3`         | Less than.                              |
| `+:3`         | Addition.                               |
| `-:3`         | Subtraction.                            |
| `*:3`         | Multiplication.                         |
| `/:3`         | Division.                               |
| `^^`          | Increment.                              |

### Comments

Use `%^` for single-line comments:
```
%^ This is a comment in Meow!
```

---

## Advanced Features

### Functions

Define reusable blocks of code using `meowmeow`:
```
meowmeow add_treats(treats, more_treats) {
    nyaa treats +:3 more_treats
}
```

### Arrays and Strings

- Create arrays:
  ```
  meow toys ~= [^.^] ["mouse", "ball", "yarn"]
  ```
- Access and manipulate strings:
  ```
  meow greeting ~= "Meow"
  meow full_greeting ~= meow_concat(greeting, " World!")
  ```

### File I/O

Write to and read from files with `pawwrite` and `pawread`:
```
pawwrite("file.txt", "Hello, Meow!")
meow content ~= pawread("file.txt")
PURR content
```

### Exception Handling

Handle errors gracefully using `pounce`, `land`, and `groom`:
```
pounce {
    meow bad_file ~= pawread("nonexistent.txt")
} land {
    PURR "Caught the error like a pro cat! 😺"
} groom {
    PURR "Always clean up after playing! 🧹"
}
```

---

## Built-In Functions

| Function       | Description                              |
|----------------|------------------------------------------|
| `nap`          | Pauses execution for a specified time.   |
| `pounce`       | Adds an item to an array.                |
| `scratch`      | Removes the last item from an array.     |
| `meow_concat`  | Concatenates two strings.                |
| `whiskers`     | Returns the length of a string/array.    |
| `claw`         | Slices a string/array.                  |
| `purr_repeat`  | Repeats a string.                       |
| `pawwrite`     | Writes content to a file.               |
| `pawread`      | Reads content from a file.              |
| `purr_sort`    | Sorts an array.                         |
| `flip_tail`    | Reverses an array.                      |
| `purr_sin`     | Computes sine of a number.              |
| `purr_cos`     | Computes cosine of a number.            |
| `purr_tan`     | Computes tangent of a number.           |
| `root_meow`    | Computes the square root of a number.   |

---

## Contributing

I welcome contributions! Feel free to open an issue or submit a pull request to improve **Meow**.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
