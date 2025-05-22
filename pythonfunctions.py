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


#4. Variable Scope
#Local variables: Defined inside a function (accessible only inside).
#Global variables: Defined outside (accessible everywhere, but need global to modify

x =110 #global variable
def modify():
    global x
    x = 300
modify()
print(x)

#Example 1: Data Validation
def validate_email(email):
    if '@' not in email or '.' not in email:
        return False
    return True
# Get user input
user_email = input("Enter your email: ")
# Validate and respond
if validate_email(user_email):
    print('Valid Email Login')
else:
    print("Enter a valid email")

#Example 2: File Processing
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."

print(count_words("sample.txt"))


# Password Generator
import random
import string

def generate_password(length):
    chars = (
        string.ascii_letters +
        string.digits +
        string.punctuation +
        'OX_zAo(29]=0cJ9l'  
    )
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Prompt user until they enter a valid length
while True:
    try:
        user_length = int(input("Enter desired password length (8–32): "))
        if 8 <= user_length <= 32:
            break
        else:
            print("Error: Password length must be between 8 and 32 characters. Try again.")
    except ValueError:
        print("Please enter a valid number.")

# Generate and display password
print("Generated password:", generate_password(user_length))
