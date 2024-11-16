# Dynamic and Static Typing in Python

# Description: Dynamic Typing in Python
# - Python is dynamically typed.
# - You don't need to declare variable types explicitly.
# - Variable types are determined at runtime and can change during execution.

# Example of Dynamic Typing in Python:
x = 10        # x is an integer
print(type(x))  # Output: <class 'int'>

x = "hello"   # x is now a string
print(type(x))  # Output: <class 'str'>

# Python allows this flexibility, but it can lead to runtime errors:
y = 10
z = "20"
# print(y + z)  # Uncommenting this will throw a TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Description: Static Typing (not natively in Python but achievable)
# - Python does not have native static typing, but you can use type hints for better code readability and debugging.
# - Type hints tell the expected type of variables, but they are not enforced by the Python interpreter.

# Example of Static Typing (via Type Hints):
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(5, 10)  # Works fine
print(result)  # Output: 15

# Errors won't be caught automatically, but tools like `mypy` can catch this:
# result = add_numbers(5, "10")  # This will throw an error in static type checkers like mypy.

# Summary:
# - Python uses dynamic typing by default.
# - You can use type hints to achieve some benefits of static typing.
