#module variable.py
# A variable created in a module is available in that module and can be accessed by importing the module.
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
# Example of a variable in a module
def get_person_info():
    return person1
# Example of using the module variable
def main_person():
    person_info = get_person_info()
    print("Person Info:", person_info)
if __name__ == "__main__":
    main_person()
# Import the module named module_variable and call the get_person_info function
import module_variable
print("Person Info:", module_variable.get_person_info())

#rename the module_variable.py to person_info.py
# Import module_variable as person_info
import module_variable as person_info
# Call the get_person_info function from the person_info module
print("Person Info:", person_info.get_person_info())

#Built-in Modules
# Python provides a rich set of built-in modules that you can use to perform various tasks.
#platform module
import platform
# Example of using the platform module to get system information
def get_system_info():
    return platform.system(), platform.release()
# Example of using the get_system_info function
def main_platform():
    system, release = get_system_info()
    print(f"System: {system}, Release: {release}")
if __name__ == "__main__":
    main_platform()
# datetime module
import datetime
# Example of using the datetime module to get the current date and time
def get_current_datetime():
    return datetime.datetime.now()
# Example of using the get_current_datetime function
def main_datetime():
    current_datetime = get_current_datetime()
    print(f"Current Date and Time: {current_datetime}")
if __name__ == "__main__":
    main_datetime()
# random module
import random
# Example of using the random module to generate a random number
def generate_random_number(start, end):
    return random.randint(start, end)
# Example of using the generate_random_number function
def main_random():
    random_number = generate_random_number(1, 100)
    print(f"Random Number: {random_number}")
if __name__ == "__main__":
    main_random()
# os module
import os
# Example of using the os module to get the current working directory
def get_current_directory():
    return os.getcwd()
# Example of using the get_current_directory function
def main_os():
    current_directory = get_current_directory()
    print(f"Current Working Directory: {current_directory}")
if __name__ == "__main__":
    main_os()
# sys module
import sys
# Example of using the sys module to get the Python version
def get_python_version():
    return sys.version
# Example of using the get_python_version function
def main_sys():
    python_version = get_python_version()
    print(f"Python Version: {python_version}")
if __name__ == "__main__":
    main_sys()
# json module
import json
# Example of using the json module to convert a Python object to a JSON string
def convert_to_json(data):
    return json.dumps(data)
# Example of using the convert_to_json function
def main_json():
    data = {"name": "Alice", "age": 30, "city": "New York"}
    json_string = convert_to_json(data)
    print(f"JSON String: {json_string}")
if __name__ == "__main__":
    main_json()
# Example of using the json module to parse a JSON string
def parse_json(json_string):
    return json.loads(json_string)
# Example of using the parse_json function
def main_parse_json():
    json_string = '{"name": "Bob", "age": 25, "city": "Los Angeles"}'
    data = parse_json(json_string)
    print(f"Parsed Data: {data}")
if __name__ == "__main__":
    main_parse_json()
#another built-in module example
# math module
import math 
# Example of using the math module to perform mathematical operations
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)
# Example of using the calculate_circle_area function
def main_math():
    radius = 5
    area = calculate_circle_area(radius)
    print(f"The area of a circle with radius {radius} is {area}")
if __name__ == "__main__":
    main_math()
# Example of using the math module to calculate the square root
def calculate_square_root(value):
    return math.sqrt(value)
# Example of using the calculate_square_root function
def main_square_root():
    value = 25
    square_root = calculate_square_root(value)
    print(f"The square root of {value} is {square_root}")
if __name__ == "__main__":
    main_square_root()
# Example of using the math module to calculate the factorial
def calculate_factorial(value):
    return math.factorial(value)
# Example of using the calculate_factorial function
def main_factorial():
    value = 5
    factorial_result = calculate_factorial(value)
    print(f"The factorial of {value} is {factorial_result}")
if __name__ == "__main__":
    main_factorial()
# Example of using the math module to calculate the power
def calculate_power(base, exponent):
    return math.pow(base, exponent)
# Example of using the calculate_power function
def main_power():
    base = 2
    exponent = 3
    power_result = calculate_power(base, exponent)
    print(f"{base} raised to the power of {exponent} is {power_result}")
if __name__ == "__main__":
    main_power()
# Example of using the math module to calculate the logarithm
def calculate_logarithm(value, base):
    return math.log(value, base)
# Example of using the calculate_logarithm function
def main_logarithm():
    value = 100
    base = 10
    logarithm_result = calculate_logarithm(value, base)
    print(f"The logarithm of {value} to the base {base} is {logarithm_result}")
if __name__ == "__main__":
    main_logarithm()
# Example of using the math module to calculate the sine of an angle
def calculate_sine(angle):
    return math.sin(math.radians(angle))
# Example of using the calculate_sine function
def main_sine():
    angle = 30
    sine_result = calculate_sine(angle)
    print(f"The sine of {angle} degrees is {sine_result}")
if __name__ == "__main__":
    main_sine()
# Example of using the math module to calculate the cosine of an angle
def calculate_cosine(angle):
    return math.cos(math.radians(angle))
# Example of using the calculate_cosine function
def main_cosine():
    angle = 60
    cosine_result = calculate_cosine(angle)
    print(f"The cosine of {angle} degrees is {cosine_result}")
if __name__ == "__main__":
    main_cosine()
# Example of using the math module to calculate the tangent of an angle
def calculate_tangent(angle):
    return math.tan(math.radians(angle))
# Example of using the calculate_tangent function
def main_tangent():
    angle = 45
    tangent_result = calculate_tangent(angle)
    print(f"The tangent of {angle} degrees is {tangent_result}")
if __name__ == "__main__":
    main_tangent()




