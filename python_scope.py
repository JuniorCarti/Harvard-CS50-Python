#python scope
#a variable is a name that refers to a value
#a variable is only available from inside the region it is created
# and the variables are available from inside any function that is in the same region
# Example of variable scope in Python
def outer_function():
    x = "local"
    
    def inner_function():
        nonlocal x  # Access the variable from the outer function
        x = "nonlocal"
        print("Inner function:", x)  # Output: Inner function: nonlocal
    
    inner_function()
    print("Outer function:", x)  # Output: Outer function: nonlocal
outer_function()
# Example of variable scope in Python with global variable
def global_function():
    global y  # Declare y as a global variable
    y = "global"
    print("Global function:", y)  # Output: Global function: global
global_function()
print("Global variable:", y)  # Output: Global variable: global
# Example of variable scope in Python with local variable
def local_function():
    z = "local"
    print("Local function:", z)  # Output: Local function: local
local_function()
# print("Local variable:", z)  # This will raise an error because z is not defined outside the function

def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)  # Output: Python is fantastic

def myfunc():
    x = 300
    print(x)
myfunc()
    