#Function Polymorphism
#An example of a Python function that can be used on different objects is the len() function.
# The len() function can be used on strings, lists, tuples, and dictionaries.
# This is an example of polymorphism, where the same function can be used on different objects. 
# Polymorphism allows for flexibility and code reuse, as the same function can be applied to different data types without needing to rewrite the function for each type.
# Function Polymorphism Example
def add(x, y):
    return x + y
# Example of function polymorphism
print(add(5, 10))        # Adding two integers
print(add(5.5, 10.2))    # Adding two floats
print(add("Hello, ", "World!"))  # Concatenating two strings
# Example of function polymorphism with lists
def add_lists(list1, list2):
    return list1 + list2
# Example of function polymorphism with tuples
def add_tuples(tuple1, tuple2):
    return tuple1 + tuple2
# Example of function polymorphism with dictionaries
def add_dicts(dict1, dict2):
    return {**dict1, **dict2}   
# Example of function polymorphism with sets
def add_sets(set1, set2):
    return set1.union(set2)
# Example of function polymorphism with custom objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
# Example of using the Point class with function polymorphism
point1 = Point(1, 2)
point2 = Point(3, 4)
point3 = point1 + point2
print(f"Point3 coordinates: ({point3.x}, {point3.y})")  # Output: Point3 coordinates: (4, 6)
# Example of function polymorphism with different data types
def print_info(data):
    if isinstance(data, str):
        print(f"String: {data}")
    elif isinstance(data, list):
        print(f"List: {data}")
    elif isinstance(data, dict):
        print(f"Dictionary: {data}")
    else:
        print("Unsupported data type")
        
    


