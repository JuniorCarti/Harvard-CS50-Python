#python modules
# A module is a file containing Python code. It can define functions, classes, and variables.
# Modules allow you to logically organize your Python code and reuse it across different programs.
# To use a module, you can import it using the import statement.
# Example of importing a module
import math
# Using the math module to perform mathematical operations
def calculate_square_root(value):
    return math.sqrt(value)
# Example of using the calculate_square_root function
def main():
    value = 16
    result = calculate_square_root(value)
    print(f"The square root of {value} is {result}")
if __name__ == "__main__":
    main()
# Example of importing a specific function from a module
from math import pow
# Using the pow function to calculate power
def calculate_power(base, exponent):
    return pow(base, exponent)
# Example of using the calculate_power function
def main_power():
    base = 2
    exponent = 3
    result = calculate_power(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}")
if __name__ == "__main__":
    main_power()
# Example of importing all functions from a module
from math import *
# Using the factorial function from the math module
def calculate_factorial(value):
    return factorial(value)
# Example of using the calculate_factorial function
def main_factorial():
    value = 5
    result = calculate_factorial(value)
    print(f"The factorial of {value} is {result}")
if __name__ == "__main__":
    main_factorial()
# Example of creating a custom module
# Create a custom module named my_module.py
# my_module.py
def greet(name):
    return f"Hello, {name}!"
# Example of using the custom module

