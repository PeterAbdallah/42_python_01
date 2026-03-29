_This project has been created as part of the 42 curriculum by pabdalla_

# Code Cultivation - Object-Oriented Garden Systems

## Evaluator Instructions

### Running the scripts
Replace with necessary values
```bash
python3 {exercise.py}
# or directly if the shebang is set:
./{exercise_path.py}
```

### Checking code standards
```bash
flake8      # style linter
mypy ./     # type checker
```

---

## Overview

This project builds a comprehensive digital garden ecosystem using Python.
It starts from basic program structure and progressively introduces
Object-Oriented Programming concepts through a series of exercises.

---

## Concepts Covered

- Structuring Python programs with `if __name__ == "__main__":`
- Organizing data using classes and objects
- Inheritance and method overriding with `super()`
- Data encapsulation and protection conventions
- Nested classes for internal system design
- Static methods and class methods
- Polymorphism through specialized subclasses
- Type hints and code standards with `mypy` and `flake8`

---

## Key Python Concepts

### Inheritance
- Subclasses inherit attributes and methods from their parent
- `super()` calls the parent's version of a method
- Method overriding allows specialized behavior per subclass

### Encapsulation
- Protected attributes use a single underscore prefix: `_attribute`
- Getters and setters control access to sensitive data
- Nested classes group internal logic that belongs to the outer class

### Static Methods
- Defined with `@staticmethod`
- Do not receive `self` or `cls` — they belong to the class but need no instance
- Used for utility logic related to the class

### Class Methods
- Defined with `@classmethod`
- Receive `cls` instead of `self` — they operate on the class itself
- Commonly used as alternative constructors

### Shebang Line
- `#!/usr/bin/env python3` as the first line of a script
- Tells the OS which interpreter to use when running the file directly
- Requires `chmod +x filename.py` to make the script executable
- Run with `./filename.py` instead of `python3 filename.py`

---
