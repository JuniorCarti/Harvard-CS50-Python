#Functions are reusable blocks of code that perform a specific task. 
#They help in organizing code, avoiding repetition, and improving readability.
#1. Function Definition & Syntax
#A function is defined using the def keyword.
#def function_name(parameters):
   # """Docstring (optional)"""
    # Function body
   # return result  # Optional
def greet(name):
    #this function greets the user
    print(f"Hello, {name}!")
greet("Alice")
        
#2. Function Parameters
#Functions can take different types of parameters:
#a. Positional Arguments (Required)
#Must be passed in the correct order.
def add(a, b):
    return a + b
print(add(5, 3))

def multiply(c, d):
    return c * d
print(multiply(5, 10))

#b. Default Arguments 
#If not provided, default values are used.
def greet(name = 'Guest'):
    print(f"Hello, {name}!")

greet()
greet("Ridge")

#c. Keyword Arguments (Named Parameters)
#Pass arguments in any order by specifying parameter names.
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")
describe_pet(name = 'Max', animal = 'cat')

#d. Arbitrary Arguments (*args)
#Accepts any number of positional arguments as a tuple.
def sum_all(*numbers):
    return sum(numbers)
print(sum_all(10, 20, 30))

def modulus(*numbers):
    # Returns the modulus of all numbers in sequence from left to right
    if not numbers:
        return None
    result = numbers[0]
    for num in numbers[1:]:
        result %= num
    return result
print(modulus(10, 20, 30))

#e. Arbitrary Keyword Arguments (**kwargs)
#Accepts any number of keyword arguments as a dictionary.
def user_info(**details):
    for key, value in details.items():
        print(f"{key}:, {value}")

user_info(name = 'Ridge', age = 23, city = 'Eldoret')

#3. Return Values
#A function can return a value using return.
#If no return is specified, it returns None.
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)  # Output: 20

#Multiple Return Values (as a Tuple)
def min_max(numbers):
    return min(numbers), max(numbers)
minimum, maximum = min_max([3, 1, 4, 2])
print(minimum, maximum)