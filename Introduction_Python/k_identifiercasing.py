# Identifier Casing in Python

# What is Identifier Casing?
# - Identifier casing refers to the naming conventions used to define identifiers like variables, functions, classes, etc.
# - It helps make code more readable and standardized.

# Common Identifier Casing Styles in Python:

# 1. Snake Case:
# - All words are in lowercase and separated by underscores (_).
# - Commonly used for variables, functions, and module names.
# Example:
snake_case_variable = "This is snake_case"

# 2. Pascal Case (a.k.a Camel Case for Classes):
# - Each word starts with an uppercase letter.
# - Commonly used for class names.
# Example:
class PascalCaseExample:
    pass

# 3. Camel Case (Lower Camel Case):
# - The first word starts with a lowercase letter, and subsequent words start with an uppercase letter.
# - Less commonly used in Python but popular in other languages like Java.
# Example:
camelCaseExample = "This is camelCase"

# 4. Upper Case (All Caps):
# - All letters are uppercase, and words are separated by underscores.
# - Used for constants.
# Example:
CONSTANT_VALUE = 42

# 5. Single or Double Leading Underscore:
# - Single leading underscore (`_var`): Indicates a private or internal variable.
# - Double leading underscore (`__var`): Used for name mangling in classes to avoid naming conflicts.
# Examples:
_internal_var = "Private variable"
class MyClass:
    def __init__(self):
        self.__private_var = "Name-mangled variable"

# 6. Double Leading and Trailing Underscores:
# - Reserved for special methods and attributes in Python (dunder methods).
# - Example: `__init__`, `__str__`
# Example:
class ExampleClass:
    def __init__(self):
        self.value = 0

# Examples of Identifier Casing in Action:

# Snake Case
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 3))  # Outputs: 15

# Pascal Case
class MyPascalCase:
    def greet(self):
        return "Hello from PascalCase!"

print(MyPascalCase().greet())  # Outputs: Hello from PascalCase!

# Constant (All Caps)
PI = 3.14159
print(PI)  # Outputs: 3.14159

# Summary:
# - Use snake_case for variables and functions.
# - Use PascalCase for class names.
# - Use ALL_CAPS for constants.
# - Avoid mixing casing styles for consistency and readability.
