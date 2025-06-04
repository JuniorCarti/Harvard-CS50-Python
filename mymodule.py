def greeting(name):
  print("Hello, " + name)

# Example of using the custom module
def main():
    name = "Alice"
    greeting(name)
if __name__ == "__main__":
    main()
#Import the module named mymodule, and call the greeting function:
import mymodule
mymodule.greeting("Alice")
# Import the module named mymodule and call the greeting function
import mymodule
mymodule.greeting("Bob")
# Import the module named mymodule and call the greeting function
import mymodule
mymodule.greeting("Charlie")
# Import the module named mymodule and call the greeting function
import mymodule 
mymodule.greeting("David")


#Variables in Module
# A variable created in a module is available in that module and can be accessed by importing the module.
# Example of a variable in a module
module_variable = "This is a module variable"
def get_module_variable():
    return module_variable
# Example of using the module variable
def main_variable():
    print("Module variable:", get_module_variable())
if __name__ == "__main__":
    main_variable()
