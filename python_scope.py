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