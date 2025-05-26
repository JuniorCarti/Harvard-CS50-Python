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