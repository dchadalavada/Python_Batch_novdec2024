# Semicolon (`;`) and Comma (`,`) in Python

# 1. Semicolon (`;`)
# - In Python, the semicolon (`;`) is not required to terminate statements.
# - However, you can use semicolons to separate multiple statements on a single line.
# - The semicolon is optional and generally discouraged in Python, as Python emphasizes readability.
# - If you write multiple statements on one line, they are separated by semicolons.

# Example of Using Semicolon:
x = 10; y = 20; z = 30  # Multiple statements on one line
print(x, y, z)  # Outputs: 10 20 30

# 2. Comma (`,`)
# - The comma is primarily used for separating items in:
#   1. Lists
#   2. Tuples
#   3. Function arguments
#   4. Multiple values in `print()` or `return` statements
# - Commas separate values or arguments in these structures.
# - The comma is essential in many data structures and function calls in Python.

# Example of Using Comma in a List:
fruits = ["apple", "banana", "cherry"]  # Elements in a list are separated by commas
print(fruits)  # Outputs: ['apple', 'banana', 'cherry']

# Example of Using Comma in a Function Call:
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
    
greet("Alice", 30)  # Arguments are separated by commas

# Example of Using Comma in a Print Statement:
print("Hello", "World", 2024)  # Multiple values are separated by commas (Outputs: Hello World 2024)

# Example of Using Comma in a Tuple:
coordinates = (10, 20, 30)  # Elements in a tuple are separated by commas
print(coordinates)  # Outputs: (10, 20, 30)

# Summary:
# - Semicolons (`;`) are rarely used in Python and are mainly for separating multiple statements on one line.
# - Commas (`,`) are used frequently in Python for separating elements in lists, tuples, function arguments, and multiple values in print statements.
# - It's recommended to use commas for separating values and avoid semicolons unless necessary for compact code.
