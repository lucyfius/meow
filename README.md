# Meow Programming Language 🐱

**A programming language for cars, if you're not a car, do not use... D:**

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Examples](#examples)
4. [Language Features](#language-features)
5. [Development](#development)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

Meow is a playful programming language that combines functionality with feline charm. Perfect for cats who code (or cars, apparently).

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/meow.git
cd meow
```

2. Ensure Python 3.7+ is installed.

3. Run the interpreter:
```bash
python src/main.py your_script.meow
```

### Running Your First Script

Create a file `hello.meow`:
```meow
meow greeting ~= "Hello from the Meow language! 🐱"
PURR greeting
HISSSS
```

## Examples

Check out our example scripts in the `examples/` directory:

- `hello_world.meow` - Basic syntax introduction
- `array_operations.meow` - Working with arrays
- `math_fun.meow` - Mathematical operations
- `file_handling.meow` - File I/O with error handling
- `string_manipulation.meow` - String operations

## Language Features

### Core Syntax
- Variables: `meow variable_name ~= value`
- Print: `PURR value`
- Exit: `HISSSS`
- Comments: `%^ This is a comment`

### Data Types
- Strings: `"Hello!"`
- Numbers: `42`, `3.14`
- Arrays: `[^.^] ["mouse", "ball", "yarn"]`

### Built-in Functions

#### Array Operations
- `pounce(array, item)` - Add item to array
- `scratch(array)` - Remove last item
- `purr_sort(array)` - Sort array
- `flip_tail(array)` - Reverse array
- `whiskers(array)` - Get array length

#### String Operations
- `meow_concat(str1, str2)` - Concatenate strings
- `purr_repeat(str, times)` - Repeat string
- `yarn_split(str, delimiter)` - Split string
- `yarn_join(array, delimiter)` - Join array elements

#### Math Operations
- `purr_sin(x)` - Sine function
- `purr_cos(x)` - Cosine function
- `root_meow(x)` - Square root
- `log_meow(x)` - Natural logarithm

#### File Operations
- `pawwrite(filename, content)` - Write to file
- `pawread(filename)` - Read from file
- `pawappend(filename, content)` - Append to file

### Error Handling
```meow
pounce {
    %^ Try block
} land {
    %^ Catch block
} groom {
    %^ Finally block
}
```

## Development

### Project Structure
```
meow/
├── src/
│   ├── interpreter/
│   │   ├── builtins/
│   │   │   ├── array_ops.py
│   │   │   ├── file_ops.py
│   │   │   ├── math_ops.py
│   │   │   └── string_ops.py
│   │   └── interpreter.py
│   ├── lexer/
│   │   ├── lexer.py
│   │   └── token_types.py
│   ├── utils/
│   │   ├── ascii_art.py
│   │   └── config.py
│   └── tests/
│       ├── test_array_ops.py
│       ├── test_file_ops.py
│       ├── test_math_ops.py
│       └── test_string_ops.py
└── examples/
    ├── hello_world.meow
    ├── array_operations.meow
    ├── math_fun.meow
    ├── file_handling.meow
    └── string_manipulation.meow
```

### Running Tests
```bash
python src/tests/run_tests.py
```

## Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License.
