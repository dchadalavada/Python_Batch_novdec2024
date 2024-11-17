# Python Built-in Functions

# Description:
# Python has several built-in functions that are always available without needing to import any module. 
# Here’s a categorized list with examples.

# 1. Input and Output:
print("Hello, World!")  # Outputs data to the console.
input("Enter your name: ")  # Takes input from the user.

# 2. Type Conversion:
int("42")        # Converts a string to an integer.
float("3.14")    # Converts a string to a float.
str(123)         # Converts a number to a string.
bool(0)          # Converts to a boolean (False in this case).

# 3. Math Functions:
abs(-10)         # Returns the absolute value: 10
round(3.14159, 2)  # Rounds to 2 decimal places: 3.14
pow(2, 3)        # Raises 2 to the power of 3: 8
max(1, 5, 3)     # Returns the maximum value: 5
min(1, 5, 3)     # Returns the minimum value: 1

# 4. String Manipulation:
len("hello")     # Returns the length of the string: 5
ord('a')         # Returns the ASCII value of 'a': 97
chr(97)          # Converts ASCII value to a character: 'a'

# 5. Data Type Helpers:
type(123)        # Returns the type of an object: <class 'int'>
isinstance(123, int)  # Checks if an object is an instance of a type: True

# 6. Iterables and Sequences:
list(range(5))   # Creates a list from 0 to 4: [0, 1, 2, 3, 4]
sum([1, 2, 3])   # Sums the elements of a list: 6
sorted([3, 1, 2])  # Returns a sorted list: [1, 2, 3]
reversed([1, 2, 3])  # Returns a reverse iterator.

# 7. Functional Programming:
map(str, [1, 2, 3])  # Converts each element to a string: ['1', '2', '3']
filter(lambda x: x > 2, [1, 2, 3])  # Filters elements greater than 2: [3]
zip([1, 2], ['a', 'b'])  # Combines two iterables: [(1, 'a'), (2, 'b')]

# 8. File Handling:
file = open("example.txt", "w")  # Opens a file in write mode.
file.write("Hello, File!")       # Writes to the file.
file.close()                     # Closes the file.

# 9. Miscellaneous:
help(len)        # Displays documentation for the `len` function.
dir(str)         # Lists attributes and methods of the `str` class.
id(123)          # Returns the unique ID of an object.
eval("3 + 5")    # Evaluates a string as Python code: 8

# Summary:
# Python provides a wide range of built-in functions for performing common tasks.
# For a complete list, check the Python documentation: https://docs.python.org/3/library/functions.html
