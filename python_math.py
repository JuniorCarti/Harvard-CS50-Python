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
# Example of using the math module to calculate the factorial of a number
def calculate_factorial(number):
    return math.factorial(number)
# Example of using the calculate_factorial function
def main_factorial():
    number = 5
    factorial = calculate_factorial(number)
    print(f"Factorial of {number}: {factorial}")
if __name__ == "__main__":
    main_factorial()
# Example of using the math module to calculate the sine of an angle
def calculate_sine(angle):
    return math.sin(math.radians(angle))
# Example of using the calculate_sine function
def main_sine():
    angle = 30
    sine_value = calculate_sine(angle)
    print(f"Sine of {angle} degrees: {sine_value}")
if __name__ == "__main__":
    main_sine()
# Example of using the math module to calculate the cosine of an angle
def calculate_cosine(angle):
    return math.cos(math.radians(angle))
# Example of using the calculate_cosine function
def main_cosine():
    angle = 60
    cosine_value = calculate_cosine(angle)
    print(f"Cosine of {angle} degrees: {cosine_value}")
if __name__ == "__main__":
    main_cosine()
# Example of using the math module to calculate the tangent of an angle
def calculate_tangent(angle):
    return math.tan(math.radians(angle))
# Example of using the calculate_tangent function
def main_tangent():
    angle = 45
    tangent_value = calculate_tangent(angle)
    print(f"Tangent of {angle} degrees: {tangent_value}")
if __name__ == "__main__":
    main_tangent()
# Example of using the math module to calculate the logarithm of a number
def calculate_logarithm(number, base=10):
    return math.log(number, base)
# Example of using the calculate_logarithm 
def main_logarithm():
    number = 100
    base = 10
    logarithm_value = calculate_logarithm(number, base)
    print(f"Logarithm of {number} to base {base}: {logarithm_value}")
if __name__ == "__main__":
    main_logarithm()
