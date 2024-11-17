# Keywords in Python

# What are Keywords?
# - Keywords are reserved words in Python that have a special meaning.
# - They are used to define the syntax and structure of Python programs.
# - You cannot use keywords as variable names, function names, or identifiers.

# Characteristics of Keywords:
# - They are case-sensitive.
# - Python has a fixed number of keywords that may vary between versions.

# Examples of Python Keywords:
# - Common keywords include: `if`, `else`, `while`, `for`, `def`, `return`, `import`, `class`, etc.

# How to See All Keywords in Python:
# - You can use the `keyword` module to get a list of all keywords.

# Example: Listing all keywords in Python
import keyword
print(keyword.kwlist)

# Examples of Using Keywords in Code:

# 1. `if`, `else`, `elif`
# - Used for conditional statements.
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

# 2. `for` and `while`
# - Used for loops.
# Example of a `for` loop:
for i in range(3):
    print(i)  # Prints numbers 0, 1, 2

# Example of a `while` loop:
count = 0
while count < 3:
    print(count)  # Prints numbers 0, 1, 2
    count += 1

# 3. `def`
# - Used to define a function.
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Outputs: Hello, Alice!

# 4. `import`
# - Used to import modules.
# Example:
import math
print(math.sqrt(16))  # Outputs: 4.0

# Reserved Python Keywords (Cannot Be Used as Identifiers):
# - `False`, `None`, `True`, `and`, `as`, `assert`, `break`, `class`, `continue`,
# - `def`, `del`, `elif`, `else`, `except`, `finally`, `for`, `from`, `global`,
# - `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `not`, `or`, `pass`,
# - `raise`, `return`, `try`, `while`, `with`, `yield`

# Note: These keywords are subject to change in future Python versions.
