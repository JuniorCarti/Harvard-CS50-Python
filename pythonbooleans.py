#python boolean
# # # Boolean values are used to represent the truth value of an expression
# # # Boolean values can be either True or False
# # # Boolean values are often used in conditional statements to control the flow of a program
# # # Boolean values are often used in logical operations to combine multiple conditions
# # # Boolean values are often used in comparison operations to compare two values
# # # Boolean values are often used in bitwise operations to manipulate individual bits
# # # Boolean values are often used in arithmetic operations to perform calculations
# # # Boolean values are often used in string operations to manipulate strings
# # # Boolean values are often used in list operations to manipulate lists
# # # Boolean values are often used in dictionary operations to manipulate dictionaries
# # # Boolean values are often used in set operations to manipulate sets
# # # Boolean values are often used in tuple operations to manipulate tuples
# # # Boolean values are often used in file operations to manipulate files
# # # Boolean values are often used in network operations to manipulate network connections
# # # Boolean values are often used in database operations to manipulate databases
# # # Boolean values are often used in GUI operations to manipulate graphical user interfaces
# # # Boolean values are often used in web operations to manipulate web pages
# # # Boolean values are often used in XML operations to manipulate XML documents
# # # Boolean values are often used in JSON operations to manipulate JSON documents
# # # Boolean values are often used in CSV operations to manipulate CSV files
# # # Boolean values are often used in YAML operations to manipulate YAML files
# # # Boolean values are often used in HTML operations to manipulate HTML documents

#meaning of > is greater than
#meaning of < is less than
print("10 > 9 is", 10 > 9)
print("10 < 9 is", 10 < 9)
#meaning of == is equal to
#meaning of != is not equal to
print("10 == 9 is", 10 == 9)
print("10 != 9 is", 10 != 9)
#meaning of >= is greater than or equal to
#meaning of <= is less than or equal to
print("10 >= 9 is", 10 >= 9)
print("10 <= 9 is", 10 <= 9)
#meaning of and is logical and
#meaning of or is logical or
#meaning of not is logical not
print("10 > 9 and 9 > 8 is", 10 > 9 and 9 > 8)
print("10 > 9 or 9 > 8 is", 10 > 9 or 9 > 8)    
print("not(10 > 9) is", not(10 > 9))
#meaning of is is identity operator
#meaning of is not is identity operator
print("10 is 9 is", 10 is 9)
print("10 is not 9 is", 10 is not 9)

#Print a message based on whether the condition is True or False:
x = 10
y = 20
if x > y:
    print("x is greater than y")
else:
    print("x is less than or equal to y")

#Check if a number is even or odd:
number = 17
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

#Check if a string is empty or not:
string = ""
if string:
    print("String is not empty")
else:
    print("String is empty")

#Check if a list is empty or not:
my_list = [1, 2, 3]
if my_list:
    print("List is not empty")
else:
    print("List is empty")
#Check if a dictionary is empty or not:
my_dict = {"key": "value"}
if my_dict:
    print("Dictionary is not empty")
else:
    print("Dictionary is empty")
#Check if a set is empty or not:
my_set = {1, 2, 3}
if my_set:
    print("Set is not empty")
else:
    print("Set is empty")
#Check if a tuple is empty or not:
my_tuple = (1, 2, 3)
if my_tuple:
    print("Tuple is not empty")
else:
    print("Tuple is empty")

#Check if a variable is None or not:
my_var = None
if my_var is None:
    print("Variable is None")
else:
    print("Variable is not None")
#Check if a variable is True or False:
my_var = True
if my_var:
    print("Variable is True")
else:
    print("Variable is False")
#Check if a variable is a string or not:
my_var = "Hello"
if isinstance(my_var, str):
    print("Variable is a string")
else:
    print("Variable is not a string")
#Check if a variable is an integer or not:
my_var = 10
if isinstance(my_var, int):
    print("Variable is an integer")
else:
    print("Variable is not an integer")
#Check if a variable is a float or not:
my_var = 10.5
if isinstance(my_var, float):
    print("Variable is a float")
else:
    print("Variable is not a float")
#Check if a variable is a list or not:
my_var = [1, 2, 3]
if isinstance(my_var, list):
    print("Variable is a list")
else:
    print("Variable is not a list")
#Check if a variable is a dictionary or not:
my_var = {"key": "value"}
if isinstance(my_var, dict):
    print("Variable is a dictionary")
else:
    print("Variable is not a dictionary")
#Check if a variable is a set or not:
my_var = {1, 2, 3}
if isinstance(my_var, set):
    print("Variable is a set")
else:
    print("Variable is not a set")
#Check if a variable is a tuple or not:
my_var = (1, 2, 3)
if isinstance(my_var, tuple):
    print("Variable is a tuple")
else:
    print("Variable is not a tuple")
#Check if a variable is a boolean or not:
my_var = True
if isinstance(my_var, bool):
    print("Variable is a boolean")
else:
    print("Variable is not a boolean")

#Evaluate Values and Variables
#The bool() function allows you to evaluate any value, and give you True or False in return,
#Example
#The following values evaluate to False:
#1. Any string, except empty strings
#2. Any number, except 0
#3. Any list, tuple, set, or dictionary, except empty ones
#4. None
#5. False
#6. Any object that is not empty
#7. Any object that is not None
#8. Any object that is not False
#9. Any object that is not 0
#10. Any object that is not an empty string
#11. Any object that is not an empty list
#12. Any object that is not an empty tuple
#13. Any object that is not an empty set
#14. Any object that is not an empty dictionary
#15. Any object that is not an empty file
#16. Any object that is not an empty array
#17. Any object that is not an empty matrix
#18. Any object that is not an empty vector
#19. Any object that is not an empty string
#20. Any object that is not an empty list
#21. Any object that is not an empty tuple
#22. Any object that is not an empty set

print(bool("Hello"))  # True
print(bool(""))  # False

x = 5
y = 0
print(bool(x))  # True
print(bool(y))  # False
print(bool([1, 2, 3]))  # True
print(bool([]))  # False
print(bool({"key": "value"}))  # True
print(bool({}))  # False
print(bool(None))  # False
print(bool(False))  # False
print(bool(True))  # True
print(bool(0))  # False
print(bool(1))  # True
print(bool(0.0))  # False
print(bool(1.0))  # True
print(bool("False"))  # True
print(bool("True"))  # True
print(bool("0"))  # True
print(bool("1"))  # True
print(bool("None"))  # True





