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
