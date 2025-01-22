# Meow Programming Language 🐱

<div align="center">

![Meow Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Test Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)

</div>

**code for cars, because when your car wants to code, you let it**

## Table of Contents

1. [Overview](#overview)
2. [System Requirements](#system-requirements)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Language Specification](#language-specification)
   - [Core Concepts](#core-concepts)
   - [Syntax Reference](#syntax-reference)
   - [Type System](#type-system)
   - [Standard Library](#standard-library)
6. [Advanced Features](#advanced-features)
7. [Development Guide](#development-guide)
8. [Testing](#testing)
9. [Performance Considerations](#performance-considerations)
10. [Security Guidelines](#security-guidelines)
11. [Contributing](#contributing)
12. [Support](#support)
13. [License](#license)

## Overview

Meow is a domain-specific language (DSL) designed for intuitive and expressive programming with a feline-inspired syntax. It combines modern programming concepts with a playful interface, making it suitable for both educational and production environments.

### Key Features

- Strong type inference system
- Built-in error handling mechanisms
- Comprehensive standard library
- First-class support for arrays and strings
- File I/O operations with safety guarantees
- Mathematical operations with precision control
- Extensive testing framework

## System Requirements

### Minimum Requirements
- Python 3.7 or higher
- 512MB RAM
- 100MB disk space

### Recommended Specifications
- Python 3.9+
- 1GB RAM
- 500MB disk space
- Unix-based operating system

## Installation

### From Source
```bash
# Clone the repository
git clone https://github.com/your-organization/meow-lang.git
cd meow-lang

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Unix
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run tests to verify installation
python src/tests/run_tests.py
```

### Using Package Manager (Coming Soon)
```bash
pip install meow-lang
```

## Quick Start

### Hello World Example
```meow
%^ Basic Hello World program
meow greeting ~= "Hello from Meow! 🐱"
PURR greeting
HISSSS
```

### Running Programs
```bash
python src/main.py path/to/your/script.meow
```

## Language Specification

### Core Concepts

#### Variables and Scope
Variables in Meow are dynamically typed but strongly checked. All variables must be declared using the `meow` keyword:

```meow
meow counter ~= 0        %^ Number type
meow name ~= "Whiskers"  %^ String type
meow toys ~= [^.^] []    %^ Array type
```

#### Operators

| Category | Operator | Description | Example |
|----------|----------|-------------|---------|
| Arithmetic | `+:3` | Addition | `x +:3 y` |
| | `-:3` | Subtraction | `x -:3 y` |
| | `*:3` | Multiplication | `x *:3 y` |
| | `/:3` | Division | `x /:3 y` |
| Comparison | `>:3` | Greater than | `x >:3 y` |
| | `<:3` | Less than | `x <:3 y` |
| | `~=` | Equality | `x ~= y` |
| Logical | `&:3` | AND | `x &:3 y` |
| | `|:3` | OR | `x |:3 y` |
| | `!:3` | NOT | `!:3 x` |

### Type System

#### Built-in Types
- **Numbers**: Integer and floating-point
- **Strings**: UTF-8 encoded
- **Arrays**: Dynamic, heterogeneous
- **Boolean**: Represented through number type

#### Type Conversion
```meow
%^ String to number
meow str_num ~= "42"
meow num ~= paw_number(str_num)

%^ Number to string
meow num ~= 42
meow str ~= paw_string(num)
```

### Standard Library

#### Array Operations
```meow
%^ Array manipulation
meow array ~= [^.^] [1, 2, 3]
pounce(array, 4)           %^ Add element
scratch(array)             %^ Remove last element
meow sorted ~= purr_sort(array)
meow reversed ~= flip_tail(array)
meow length ~= whiskers(array)
```

#### String Operations
```meow
%^ String manipulation
meow str1 ~= "Hello"
meow str2 ~= "World"
meow result ~= meow_concat(str1, " ", str2)
meow parts ~= yarn_split(result, " ")
meow joined ~= yarn_join(parts, "-")
```

#### File Operations
```meow
%^ File handling with error checking
pounce {
    pawwrite("data.txt", "Important data")
    meow content ~= pawread("data.txt")
    pawappend("data.txt", "\nMore data")
} land {
    PURR "Error handling files! 😿"
} groom {
    PURR "Cleanup complete"
}
```

## Advanced Features

### Error Handling
Meow provides a comprehensive error handling system:

```meow
pounce {
    %^ Risky operation
    meow result ~= dangerous_operation()
} land {
    %^ Error handling
    PURR "An error occurred!"
} groom {
    %^ Cleanup
    cleanup_resources()
}
```

### Memory Management
- Automatic garbage collection
- Reference counting for resource management
- Deterministic resource cleanup

## Development Guide

### Project Structure
```
meow/
├── docs/
│   ├── api/
│   ├── examples/
│   └── tutorials/
├── src/
│   ├── interpreter/
│   ├── lexer/
│   ├── utils/
│   └── tests/
├── examples/
├── scripts/
├── requirements.txt
└── README.md
```

### Code Style Guidelines
- Use meaningful variable names
- Comment complex operations
- Follow the Meow naming conventions
- Keep functions small and focused

### Development Workflow
1. Fork the repository
2. Create a feature branch
3. Write tests
4. Implement changes
5. Run test suite
6. Submit pull request

## Testing

### Running Tests
```bash
# Run all tests
python src/tests/run_tests.py

# Run specific test category
python src/tests/run_tests.py --category array_ops
```

### Test Coverage
```bash
# Generate coverage report
coverage run -m src.tests.run_tests
coverage report
```

## Performance Considerations

### Optimization Tips
- Use array operations instead of loops where possible
- Minimize file I/O operations
- Leverage built-in functions
- Consider memory usage with large datasets

### Benchmarking
```bash
python scripts/benchmark.py your_script.meow
```

## Security Guidelines

### Best Practices
- Validate all file paths
- Sanitize input data
- Use error handling for all I/O operations
- Follow principle of least privilege

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on:
- Code of Conduct
- Development process
- Pull request requirements
- Coding standards

## Support

- Documentation: [www.lota.dev](https://www.lota.dev)
- Issues: GitHub Issues
- Community: [www.lota.dev](https://www.lota.dev)
- Email: [me@lota.dev](mailto:me@lota.dev)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
Made with 😺 by the Meow Language Team
</div>
