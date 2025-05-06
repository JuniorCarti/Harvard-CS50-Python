#variables  
# # Variables are containers for storing data values.
# # In Python, variables do not need to be declared with any particular type and can even change type after they have been set.
# # Variables do not need to be declared with any particular type and can even change type after they have been set.
# # Variables can be assigned values using the assignment operator (=).
# # The variable name can be any combination of letters, numbers, and underscores, but it cannot start with a number.
# # Variable names are case-sensitive, meaning that "myVar" and "myvar" are considered different variables.
# # Python Variables
#x = 5
#y = "Hello World"
#print(x)
#print(y)  # integer
# Variable names should be descriptive and meaningful to make the code more readable.
# It is a good practice to use lowercase letters for variable names and separate words with underscores (e.g., my_variable).
#x = 4
#x = "John"
#print(x)


# # However, it is also common to use camelCase (e.g., myVariable) in some coding styles.
# # Python is case-sensitive, so "myVar" and "myvar" are different variables.
# # Python allows you to assign multiple variables at once, like this:
# # x, y, z = 1, 2, 3
#x, y, z = 1, 2, 3
# # This assigns 1 to x, 2 to y, and 3 to z.
#print(x, y, z)
# # You can also assign the same value to multiple variables in one line:
# # x = y = z = 0
#x = y = z = 0
# # This assigns 0 to x, y, and z.
#print(x, y, z)

#Casting Variables
# # Casting is the process of converting a variable from one type to another.   
# # Python has several built-in functions for this purpose:
# # int() - converts to an integer
# # float() - converts to a floating-point number
# # str() - converts to a string
# # Example:
# x = 5
# y = "John"    
# z = 3.14
#x = 5
#y = "John"
#z = 3.14

#print(x + y)  # This will cause an error because you cannot add an integer and a string.

# # print(x + y)  # This will cause an error because you cannot add an integer and a string.
# # To fix this, you can cast the integer to a string:
# print(str(x) + y)  # Output: "5John"
#print(str(x) + y)  # Output: "5John"
# # You can also cast the string to an integer:
# y = int(y)  # This will cause an error because "John" cannot be converted to an integer.
# # To fix this, you can use a valid integer string:
# y = "10"
# y = int(y)  # Now this will work.
#y = "10"
#y = int(y)  # Now this will work.
#print(x + y)  # Output: 15
# # You can also cast the float to an integer:
# z = int(z)  # This will truncate the decimal part.
# # Now z will be 3.
#z = int(z)  # This will truncate the decimal part.
# # Now z will be 3.
#print(z)  # Output: 3
#Get the Type of a Variable
# # You can use the type() function to get the type of a variable:
# # Example:
# x = 5
# y = "John"
# z = 3.
x = 5
y = "John"
z = 3.14
# # You can also use the type() function to check the type of a variable:
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'str'>
print(type(z))  # Output: <class 'float'>
#
# print(type(x))  # Output: <class 'int'>
# print(type(y))  # Output: <class 'str'>
# print(type(z))  # Output: <class 'float'>
# # You can also use the type() function to check the type of a variable:
# # Example:
# x = 5
# print(type(x))  # Output: <class 'int'>   
# x = "Hello, World!"  # string
# print(type(x))  # Output: <class 'str'>   

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
#Output: Orange Orange Orange