# The Power of print() in Python

# 1. Basic Usage:
# - The `print()` function outputs text or data to the console.
print("Hello, World!")  # Output: Hello, World!

# 2. Printing Variables:
# - You can print the value of variables.
name = "Alice"
print(name)  # Output: Alice

# 3. Printing Multiple Values:
# - `print()` can take multiple arguments, separated by commas.
age = 25
print("Name:", name, "Age:", age)  # Output: Name: Alice Age: 25

# 4. Using `sep` to Change Separators:
# - By default, values are separated by a space, but you can customize this with the `sep` argument.
print("Python", "is", "fun", sep="-")  # Output: Python-is-fun

# 5. Using `end` to Change Line Endings:
# - By default, `print()` ends with a newline. You can change this using the `end` argument.
print("Hello", end=", ")
print("World!")  # Output: Hello, World!

# 6. Formatting Strings:
# - You can use formatted strings to make output more readable.
score = 95
print(f"Your score is {score}.")  # Output: Your score is 95.

# 7. Printing Complex Data Structures:
# - You can print lists, dictionaries, or any other data type directly.
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# 8. Debugging with print():
# - `print()` is a helpful tool for debugging by showing the values of variables at different points.
x = 10
y = 20
print("x =", x, "y =", y)  # Output: x = 10 y = 20

# 9. Printing Unicode Characters:
# - `print()` supports Unicode, allowing you to print emojis or characters from different languages.
print("Smile! 😊")  # Output: Smile! 😊
print("こんにちは (Hello in Japanese)")  # Output: こんにちは (Hello in Japanese)
print("నమస్తే (Hello in Telugu)")
print("Hola (Hello in Spanish)")
# 10. Redirecting Output:
# - The `print()` output can be redirected to files or logs.
with open("output.txt", "w") as file:
    print("Saving this to a file.", file=file)
# This writes "Saving this to a file." into `output.txt`.

# Summary:
# - `print()` is a simple yet essential tool for communicating with users, debugging, and displaying information.
# - It’s flexible, supports customization, and works with any data type!
