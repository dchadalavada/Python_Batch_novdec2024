# Multiline Statements in Python

# What Are Multiline Statements?
# - Python generally requires each statement to be written on a single line.
# - However, if a statement is too long, it can be split across multiple lines for better readability.
# - Multiline statements can be achieved in Python using:
#   1. Explicit line continuation (backslash `\`).
#   2. Implicit line continuation (using parentheses, brackets, or braces).

# 1. Explicit Line Continuation
# - Use a backslash (`\`) to indicate that the statement continues on the next line.
# - Example:
total_sum = 1 + 2 + 3 + \
            4 + 5 + 6
print(total_sum)  # Outputs: 21

# 2. Implicit Line Continuation
# - Parentheses `()`, brackets `[]`, or braces `{}` automatically allow multiline statements.
# - No backslash is needed when using these.
# - Examples:

# Using Parentheses
result = (1 + 2 + 3 +
          4 + 5 + 6)
print(result)  # Outputs: 21

# Using Brackets
colors = [
    "red", 
    "blue", 
    "green", 
    "yellow"
]
print(colors)  # Outputs: ['red', 'blue', 'green', 'yellow']

# Using Braces
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)  # Outputs: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Multiline Statements in Loops or Conditionals
# - Indentation and structure must still follow Python's rules.
# - Example:
numbers = [1, 2, 3, 4, 5]
total = sum(
    number for number in numbers
    if number % 2 == 0
)
print(total)  # Outputs: 6 (sum of even numbers)

# Summary:
# - Use backslash `\` for explicit line continuation.
# - Use parentheses `()`, brackets `[]`, or braces `{}` for implicit line continuation.
# - Aim for readability when breaking long statements into multiple lines.
