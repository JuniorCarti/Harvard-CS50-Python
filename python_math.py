#python math
# Python Math
import math
# Example of using the math module to calculate the square root of a number
def calculate_square_root(number):
    return math.sqrt(number)
# Example of using the calculate_square_root function
def main_square_root():
    number = 16
    square_root = calculate_square_root(number)
    print(f"Square Root of {number}: {square_root}")    
if __name__ == "__main__":
    main_square_root()