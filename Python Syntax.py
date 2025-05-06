# Python Syntax

"""
Python Indentation
Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, 
the indentation in Python is very important.
Python uses indentation to indicate a block of code.
"""
if 5 > 2:
    print("Five is greater than two!")  # indented code block
# The number of spaces is up to you as a programmer, but it has to be at least one space.   
# Python will give you an error if you skip the indentation.
#if 5 > 2:
#print("Five is greater than two!")  # This will cause an error because the print statement is not indented.
# Python Variables
# Variables are containers for storing data values.
# In Python, variables do not need to be declared with any particular type and can even change type after they have been set.
# Variables do not need to be declared with any particular type and can even change type after they have been set.
# Variables can be assigned values using the assignment operator (=).
# The variable name can be any combination of letters, numbers, and underscores, but it cannot start with a number.
# Variable names are case-sensitive, meaning that "myVar" and "myvar" are considered different variables.
#Python Variables
x = 5
y = "Hello World" 
print(x)
print(y)  # integer
# Variable names should be descriptive and meaningful to make the code more readable.
# It is a good practice to use lowercase letters for variable names and separate words with underscores (e.g., my_variable).
# However, it is also common to use camelCase (e.g., myVariable) in some coding styles.
# Python is case-sensitive, so "myVar" and "myvar" are different variables.
# Python allows you to assign multiple variables at once, like this:
# x, y, z = 1, 2, 3
# This assigns 1 to x, 2 to y, and 3 to z.
# You can also assign the same value to multiple variables in one line:
# x = y = z = 0 
# This assigns 0 to x, y, and z.
# You can also use the type() function to check the type of a variable:
# x = 5
# print(type(x))  # Output: <class 'int'>
# x = "Hello, World!"  # string
# print(type(x))  # Output: <class 'str'>