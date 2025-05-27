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

#Removing Array Elements
# You can remove elements from an array using the del statement or the pop() method.
# Example of removing an element using del
del cars[1]  # Removes the second car (Honda Civic)
print(cars)  # Output: [{'make': 'Toyota', 'model': 'Camry', 'year': 2020}, {'make': 'Ford', 'model': 'Focus', 'year': 2019}]
# Example of removing an element using pop
removed_car = cars.pop(0)  # Removes the first car (Toyota Camry)
print(removed_car)  # Output: {'make': 'Toyota', 'model': 'Camry', 'year': 2020}
print(cars)  # Output: [{'make': 'Ford', 'model': 'Focus', 'year': 2019}]
# Example of using numpy arrays for data processing
raw_data = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
processed_data = [data * 2 for data in raw_data]  # Example transformation
print(processed_data)  # Output: [array([2, 4, 6]), array([ 8, 10, 12]), array([14, 16, 18])]
# Example of using numpy arrays for numerical data
numbers = np.array([1, 2, 3, 4, 5])
# Accessing elements in the numpy array
print(numbers[0])  # Output: 1
print(numbers[1:3])  # Output: [2 3]
# Example of using numpy arrays for mathematical operations
# Performing mathematical operations on numpy arrays
squared_numbers = numbers ** 2
print(squared_numbers)  # Output: [ 1  4  9 16 25]
# Example of using numpy arrays for statistical operations  
mean_value = np.mean(numbers)
print(mean_value)  # Output: 3.0
# Example of using numpy arrays for statistical operations
median_value = np.median(numbers)
print(median_value)  # Output: 3.0
# Example of using numpy arrays for statistical operations
std_deviation = np.std(numbers)
print(std_deviation)  # Output: 1.4142135623730951
# Example of using numpy arrays for statistical operations
variance_value = np.var(numbers)
print(variance_value)  # Output: 2.0
# Example of using numpy arrays for statistical operations
# Performing element-wise operations on numpy arrays

# Data Processing with Lists
# Example of using lists for data processing
data = [
    {'source1': 'data1', 'source2': 'data2'},
    {'source3': 'data3', 'source4': 'data4'},
    {'source5': 'data5', 'source6': 'data6'}
]
# Processing the data
processed_data = []
for item in data:
    processed_item = {key: value.upper() for key, value in item.items()}  # Example transformation
    processed_data.append(processed_item)
print(processed_data)  # Output: [{'source1': 'DATA1', 'source2': 'DATA2'}, {'source3': 'DATA3', 'source4': 'DATA4'}, {'source5': 'DATA5', 'source6': 'DATA6'}]

# Processing temperature readings
temperatures = [22.5, 23.7, 24.8, 21.9, 20.5]
avg_temp = sum(temperatures) / len(temperatures)
high_temp = max(temperatures)
print(f"Average Temperature: {avg_temp:.2f}°C")  # Output: Average Temperature: 22.68°C
print(f"Highest Temperature: {high_temp:.2f}°C")  # Output: Highest Temperature: 24.80°C

# Example of using numpy arrays for data processing
import numpy as np
# Creating a numpy array for temperature readings
temperature_data = np.array([22.5, 23.7, 24.8, 21.9, 20.5])
# Calculating average and highest temperature using numpy
avg_temp_np = np.mean(temperature_data)
high_temp_np = np.max(temperature_data)
print(f"Average Temperature (numpy): {avg_temp_np:.2f}°C")  # Output: Average Temperature (numpy): 22.68°C
print(f"Highest Temperature (numpy): {high_temp_np:.2f}°C")  # Output: Highest Temperature (numpy): 24.80°C

