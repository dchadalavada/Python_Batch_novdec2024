# Python Comments: 

# What Are Comments in Python?
# Comments are lines in your code that Python ignores when running the program.
# They are used to:
# - Explain the code.
# - Make it more readable.
# - Temporarily disable code.

# Types of Comments in Python:

# Single-Line Comments:
# Start with a #
# Everything after # on that line is treated as a comment.

# Example:
# This is a single-line comment
print("Hello, World!")  # This prints "Hello, World!")

# Multi-Line Comments:
# Use multiple # symbols.
# Or use triple quotes (''' or """) for larger comments.

# Example 1 (Multiple # Symbols):
# This is a comment
# that spans multiple lines
print("Python is fun!")

# Example 2 (Triple Quotes):
"""
This is a multi-line comment.
It spans multiple lines.
"""
print("Learning comments!")

# Why Use Comments?
# - To document why something is done.
# - To make your code easy to understand for you and others.
# - To debug or temporarily disable code without deleting it.

# Good vs. Bad Comments:

# Bad Comment:
# x = x + 1  # Increment x

# Good Comment:
# x = x + 1  # Adjust counter to include the current iteration

# Practice:

# Try adding comments to this code:
# Step 1: Get user input
name = input("Enter your name: ")

# Step 2: Print a greeting message
print(f"Hello, {name}!")
