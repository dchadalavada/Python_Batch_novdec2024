# Identifiers in Python

# What Are Identifiers?
# - Identifiers are the names used to identify variables, functions, classes, or other objects in Python.
# - They help us refer to values or code elements in the program.

# Rules for Defining Identifiers:
# 1. Identifiers can consist of letters (A-Z, a-z), digits (0-9), and underscores (_).
# 2. They must begin with a letter or an underscore (_) but cannot start with a digit.
#    - Valid: `variable`, `_value`
#    - Invalid: `1variable`, `#name`
# 3. Identifiers are case-sensitive.
#    - `MyVar`, `myvar`, and `MYVAR` are considered different identifiers.
# 4. Keywords cannot be used as identifiers.
#    - Invalid: `def = 5`, `if = "hello"`
# 5. Special characters (like `@`, `#`, `$`, etc.) are not allowed in identifiers.
#    - Invalid: `var@name`, `my#var`

# Naming Conventions (Best Practices):
# - Use descriptive names for readability.
#   - Example: `total_amount` instead of `x`.
# - Use underscores to separate words in a name (snake_case) for variables and functions.
#   - Example: `calculate_area`.
# - For class names, use PascalCase.
#   - Example: `EmployeeDetails`.

# Examples of Valid and Invalid Identifiers:

# Valid Identifiers:
my_variable = 10
_value = 20
Number123 = 30
print(my_variable, _value, Number123)  # Outputs: 10 20 30

# Invalid Identifiers:
# 1variable = 50  # Error: Cannot start with a digit
# def = 100       # Error: Cannot use a keyword
# my-var = 200    # Error: Special characters are not allowed

# Case Sensitivity:
# - Python treats identifiers with different cases as separate.
Variable = 10
variable = 20
print(Variable, variable)  # Outputs: 10 20

# Summary:
# - Identifiers are names for elements in your program.
# - Follow rules and best practices for clear and error-free code.
# - Avoid using reserved keywords or invalid characters in identifiers.
