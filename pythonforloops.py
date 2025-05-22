#Python For Loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#For loops in Python are control flow statements that allow you to repeatedly execute 
#a block of code for each item in a sequence (like lists, tuples, strings, etc.). 
# They follow this basic syntax:
#for item in iterable:
    # code to execute
#Core Components
#1. The Iterable
#Any Python object capable of returning its members one at a time:
"""Lists: [1, 2, 3]
Strings: "Hello"
Tuples: (1, 2, 3)
Dictionaries: {'a': 1, 'b': 2}
Sets: {1, 2, 3}
Range objects: range(5)
File objects
Generators"""
"""2. The Iterator Protocol
Python's for loops work through the iterator protocol:
Calls iter() on the iterable to get an iterator
Repeatedly calls next() on the iterator
Stops when StopIteration is raised"""

#1. Looping through a sequence
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

#2. Looping a specific number of times
for i in range(3):  # 0, 1, 2
    print("Hello")
#3. Looping with index and value
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
#4. Looping through dictionary items
person = {'name': 'John', 'age': 30}
for key, value in person.items():
    print(key, value)

#Advanced For Loop Techniques
#1. Nested Loops
for i in range(3):
    for j in range(2):
        print(i, j)
#2. Loop Control Statements
#break: Exit the loop
#continue: Skip to next iteration
#else: Execute if loop completes normally
for num in range(10):
    if num == 5:
        break
    print(num)
else:
    print("Loop completed")

#3. Zip for parallel iteration
names = ['Alice: ', 'Bob: ']
ages = [22, 30]
for name, age in zip(names, ages):
    print(name, age)

#4. List Comprehensions (compact loops)
squares = [x**2 for x in range(10)]

#1. Data Processing Pipeline (ETL)
## Extract raw data from multiple sources
raw_data_sources = [
    'sales_2025.csv',
    'inventory.db',
    'customer_api.json'
]