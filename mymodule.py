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