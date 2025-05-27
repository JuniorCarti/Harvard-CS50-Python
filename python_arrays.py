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

cars = [   {'make': 'Toyota', 'model': 'Camry', 'year': 2020},]