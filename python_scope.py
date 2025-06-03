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

#Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#Global Scope
# A variable created in the main body of the Python code is a global variable.
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()
# Global variables can be accessed from any function in the same module
# and can be modified using the global keyword.
# Example of modifying a global variable
def modify_global():
    global x
    x = "fantastic"
    print("Modified global variable:", x)
modify_global()
print("Global variable after modification:", x)  # Output: Global variable after modification: fantastic
# Example of local scope
def local_scope_example():
    y = "local"
    print("Local variable:", y)  # Output: Local variable: local
local_scope_example()
# Attempting to access a local variable outside its scope will raise an error
# print("Local variable outside function:", y)  # This will raise an error because y is not defined outside the function
# Example of nonlocal scope
def outer_nonlocal():
    z = "outer"
    
    def inner_nonlocal():
        nonlocal z  # Access the variable from the outer function
        z = "inner"
        print("Inner nonlocal function:", z)  # Output: Inner nonlocal function: inner
    
    inner_nonlocal()
    print("Outer nonlocal function:", z)  # Output: Outer nonlocal function: inner

#local scope
#A variable created inside a function belongs to the local scope of that function, 
# and can only be used inside that function.
#Example
#A variable created inside a function is available inside that function:\
def myfunc():
  x = 300
  print(x)

myfunc()