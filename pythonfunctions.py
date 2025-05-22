#Functions are reusable blocks of code that perform a specific task. 
#They help in organizing code, avoiding repetition, and improving readability.
#1. Function Definition & Syntax
#A function is defined using the def keyword.
#def function_name(parameters):
   # """Docstring (optional)"""
    # Function body
   # return result  # Optional
def greet(name):
    #this function greets the user
    print(f"Hello, {name}!")
greet("Alice")
        
#2. Function Parameters
#Functions can take different types of parameters:
#a. Positional Arguments (Required)
#Must be passed in the correct order.
def add(a, b):
    return a + b
print(add(5, 3))

def multiply(c, d):
    return c * d
print(multiply(5, 10))