# IndentationError in Python

# Description:
# - Python relies on indentation (spaces or tabs) to define the structure of the code.
# - Unlike some other programming languages that use curly braces `{}` or keywords like `end`, Python uses **whitespace**.
# - If the indentation is incorrect or inconsistent, Python will raise an `IndentationError`.

# Example of IndentationError:
# This code will throw an IndentationError because the print statement is not indented properly:
def greet():
    print("Hello, world!")  # IndentationError: expected an indented block

# Correctly Indented Code:
# - The print statement should be indented to show it belongs to the `greet` function:
def greet():
    print("Hello, world!")  # Proper indentation (4 spaces is common in Python)

greet()  # Output: Hello, world!

# Common Causes of IndentationError:
# 1. Mixing spaces and tabs in the same block.
# 2. Forgetting to indent after a colon `:`.
# 3. Incorrect alignment of blocks within loops, functions, or conditionals.

# Example of Mixing Spaces and Tabs (causes an error):
def example():
    print("This line uses spaces")
    
print("This line uses tabs")  # IndentationError: unexpected indent

# Fix: Use consistent indentation (preferably 4 spaces per level):
def example():
    print("This line uses spaces")
    print("This line also uses spaces")  # Consistent indentation

# Tips to Avoid IndentationError:
# - Use a code editor that highlights indentation issues (e.g., VS Code, PyCharm).
# - Configure your editor to use 4 spaces instead of tabs.
# - Avoid manually mixing spaces and tabs.
