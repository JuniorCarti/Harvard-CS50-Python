#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#     return lambda name: f"{greeting}, {name}!"    
#Basic syntax
#lambda arguments: expression
#The expression is executed and the result is returned:
x = lambda a : a + 10
print(x(5))

#Lambda functions can take any number of arguments:
#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

#Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(10, 20, 30))

#Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, 
#and that argument will be multiplied with an unknown number:
def myfunc(n):
    return lambda a: a * n

#Use that function definition to make a function that always doubles the number you send in:
mydoubler = myfunc(2)
print(mydoubler(11))

#Or, use the same function definition to make a function that always triples the number you send in:
mytripler = myfunc(3)
print(mytripler(11))

#Or, use the same function definition to make both functions, in the same program:
mydoubler = myfunc(4)
mytripler = myfunc(5)

print(mydoubler(50))
print(mytripler(60))
# Lambda Functions in Python
# Lambda functions are small anonymous functions defined with the `lambda` keyword.
# They can take any number of arguments but can only have one expression.
# Lambda functions are often used for short, throwaway functions that are not reused elsewhere.
# Example of a simple lambda function
# Sorting with Lambda Functions
# Sorting a list of numbers in ascending order
numbers = [5, 2, 9, 1, 5, 6]
numbers_sorted = sorted(numbers, key=lambda x: x)
print(numbers_sorted)
# Output: [1, 2, 5, 5, 6, 9]
# Sorting a list of strings by their length
strings = ['apple', 'banana', 'cherry', 'date']
strings_sorted = sorted(strings, key=lambda x: len(x))
print(strings_sorted)
# Output: ['date', 'apple', 'banana', 'cherry']
students = ['Alice', 'Bob', 'Charlie', 'David']
# Sorting a list of students by their names in reverse order
students_sorted = sorted(students, key=lambda x: x, reverse=True)
print(students_sorted)


#sorting with custom keys
# Sorting a list of tuples by the second element
students = [('Alice', 88), ('Bob', 95), ('Charlie', 78)]
students_sorted = sorted(students, key=lambda x: x[1])
print(students_sorted)
# Output: [('Charlie', 78), ('Alice', 88), ('Bob', 95)]

#2. Filtering Data
# Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Output: [2, 4, 6, 8]

#Dynamic Default Values in Dictionaries
# Using defaultdict with lambda to provide default values
from collections import defaultdict

inventory = defaultdict(lambda: 'Product not available')
inventory['apple'] = 50
print(inventory['apple'])  # 50
print(inventory['orange'])  # 'Product not available'

#3. Mapping Data
# Mapping a list of numbers to their squares
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]
# Mapping a list of strings to their lengths
strings = ['apple', 'banana', 'cherry']
lengths = list(map(lambda x: len(x), strings))
print(lengths)
# Output: [5, 6, 6]
# Mapping a list of tuples to their sums
tuples = [(1, 2), (3, 4), (5, 6)]
sums = list(map(lambda x: sum(x), tuples))
print(sums)
# Output: [3, 7, 11]
# Using Lambda Functions with Higher-Order Functions
# Higher-order functions are functions that take other functions as arguments or return them as results.
# Example of a higher-order function
def apply_function(func, data):
    return [func(x) for x in data]

# Using a lambda function with a higher-order function
result = apply_function(lambda x: x ** 2, [1, 2, 3, 4])
print(result)
# Output: [1, 4, 9, 16]
# Example of using lambda functions with map and filter
def process_data(data):
    # Filtering even numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, data))
    
    # Mapping to squares
    squared_numbers = list(map(lambda x: x ** 2, even_numbers))
    
    return squared_numbers  


