#python arrays
#Arrays are used to store multiple values in one single variable:
#     {'source1': 'data1', 'source2': 'data2'}
#     {'source3': 'data3', 'source4': 'data4'}
#     {'source5': 'data5', 'source6': 'data6'}
# ]"""
# import numpy as np
# raw_data = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
# processed_data = [data * 2 for data in raw_data]  # Example transformation
# print(processed_data)  # Output: [array([2, 4, 6]), array([ 8, 10, 12]), array([14, 16, 18])]
# Example of using numpy arrays for data processing

#What is an Array?
# An array is a data structure that can hold multiple values of the same type.
# In Python, the most common way to create arrays is by using lists or the numpy library.
#An array is a special variable, which can hold more than one value at a time.
#If you have a list of items (a list of car names, for example), 
# storing the cars in single variables could look like this:
cars = ['Toyota', 'Honda', 'Ford', 'Chevrolet']
# However, this is not efficient for larger datasets.
# Instead, you can use an array to store multiple values in a single variable.
# Example of using a list to store car information
#However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
#The solution is an array!
#An array can hold many values under a single name, and you can access the values by referring to an index number.
# Example of using a list to store car information

cars = [   {'make': 'Toyota', 'model': 'Camry', 'year': 2020},]

#Access the Elements of an Array
# You can access elements in an array using their index.
# The index starts at 0, so the first element is at index 0.
print(cars[0])  # Output: {'make': 'Toyota', 'model': 'Camry', 'year': 2020}
# You can also access specific attributes of the car
print(cars[0]['make'])  # Output: Toyota
# You can loop through the array to access all elements
for car in cars:
    print(f"Make: {car['make']}, Model: {car['model']}, Year: {car['year']}")   
# Output: Make: Toyota, Model: Camry, Year: 2020
# Adding more cars to the array
cars.append({'make': 'Honda', 'model': 'Civic', 'year': 2021})
cars.append({'make': 'Ford', 'model': 'Focus', 'year': 2019})
print(cars)

# Looping through the updated array
for car in cars:
    print(f"Make: {car['make']}, Model: {car['model']}, Year: {car['year']}")
# Output:
# Make: Toyota, Model: Camry, Year: 2020
# Make: Honda, Model: Civic, Year: 2021
# Make: Ford, Model: Focus, Year: 2019
# Example of using numpy arrays for numerical data
import numpy as np
# Creating a numpy array
numbers = np.array([1, 2, 3, 4, 5])
# Accessing elements in the numpy array
print(numbers[0])  # Output: 1
print(numbers[1:3])  # Output: [2 3]
#The Length of an Array
# You can find the length of an array using the len() function.
print(len(cars))  # Output: 3 (after adding more cars)
