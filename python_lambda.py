#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#Sysntax
# lambda arguments: expression
def add(x, y):
    return x + y
add_lambda = lambda x, y: x + y
print(add(5, 3))  # Output: 8
print(add_lambda(5, 3))  # Output: 8
# Lambda functions can be used wherever function objects are required.
# They are syntactically restricted to a single expression.
# This makes them less general than a def statement, but they can be more concise.
# Lambda functions are often used for short, throwaway functions.
# They are commonly used in functional programming constructs like map, filter, and reduce.
# Example of using lambda with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
# Example of using lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
# Example of using lambda with reduce
from functools import reduce
def add_numbers(x, y):
    return x + y    
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15
# Example of using lambda with sorted
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_people = sorted(people, key=lambda person: person['age'])
print(sorted_people)  # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
# Example of using lambda with a custom function
def apply_function(func, value):
    return func(value)
result = apply_function(lambda x: x * 2, 10)
print(result)  # Output: 20
# Example of using lambda with a custom function that takes multiple arguments
def apply_function_with_args(func, *args):
    return func(*args)
result_with_args = apply_function_with_args(lambda x, y: x + y, 5, 10)
print(result_with_args)  # Output: 15
# Example of using lambda with a custom function that takes keyword arguments
def apply_function_with_kwargs(func, **kwargs):
    return func(**kwargs)
result_with_kwargs = apply_function_with_kwargs(lambda name, age: f"{name} is {age} years old", name='Alice', age=30)
print(result_with_kwargs)  # Output: Alice is 30 years old
# Example of using lambda with a custom function that returns a function
def make_multiplier(factor):
    return lambda x: x * factor
multiplier = make_multiplier(3)
result_multiplier = multiplier(10)
print(result_multiplier)  # Output: 30
# Example of using lambda with a custom function that returns a function with multiple arguments
def make_adder(x):
    return lambda y: x + y
adder = make_adder(5)
result_adder = adder(10)
print(result_adder)  # Output: 15
# Example of using lambda with a custom function that returns a function with keyword arguments
def make_greeter(greeting):
    return lambda name: f"{greeting}, {name}!"
greeter = make_greeter("Hello")
result_greeter = greeter("Alice")
print(result_greeter)  # Output: Hello, Alice!
# Example of using lambda with a custom function that returns a function with multiple keyword arguments
def make_person_info(name, age):
    return lambda city: f"{name} is {age} years old and lives in {city}."   
person_info = make_person_info("Alice", 30)
result_person_info = person_info("New York")
print(result_person_info)  # Output: Alice is 30 years old and lives in New York.
# Example of using lambda with a custom function that returns a function with default arguments
def make_default_greeter(greeting="Hello"):
    return lambda name: f"{greeting}, {name}!"
default_greeter = make_default_greeter()
result_default_greeter = default_greeter("Bob")
print(result_default_greeter)  # Output: Hello, Bob!
# Example of using lambda with a custom function that returns a function with default arguments and multiple parameters
def make_custom_greeter(greeting="Hi", punctuation="!"):
    return lambda name: f"{greeting}, {name}{punctuation}"  
custom_greeter = make_custom_greeter("Hey", "?")
result_custom_greeter = custom_greeter("Charlie")
print(result_custom_greeter)  # Output: Hey, Charlie?
# Example of using lambda with a custom function that returns a function with variable-length arguments
def make_sum_function(*args):
    return lambda: sum(args)
sum_function = make_sum_function(1, 2, 3, 4, 5)
result_sum_function = sum_function()
print(result_sum_function)  # Output: 15
# Example of using lambda with a custom function that returns a function with variable-length keyword arguments
def make_info_function(**kwargs):
    return lambda: ", ".join(f"{key}: {value}" for key, value in kwargs.items())
info_function = make_info_function(name="Alice", age=30, city="New York")
result_info_function = info_function()
print(result_info_function)  # Output: name: Alice, age: 30, city: New York