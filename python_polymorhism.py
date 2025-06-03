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
# Example of using the print_info function with different data types
print_info("Hello, World!")  # String: Hello, World!
print_info([1, 2, 3])        # List: [1, 2, 3]
print_info({"key": "value"})  # Dictionary: {'key': 'value'}
# Example of function polymorphism with different data types
def calculate_area(shape):
    if isinstance(shape, Circle):
        return 3.14 * shape.radius ** 2
    elif isinstance(shape, Rectangle):
        return shape.length * shape.width
    else:
        raise ValueError("Unsupported shape type")
class Circle:
    def __init__(self, radius):
        self.radius = radius
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
# Example of using the calculate_area function with different shape
circle = Circle(5)
rectangle = Rectangle(4, 6)
print(f"Circle area: {calculate_area(circle)}")        # Output: Circle area: 78.5
print(f"Rectangle area: {calculate_area(rectangle)}")  # Output: Rectangle area: 24
# Example of function polymorphism with different data types
def process_data(data):
    if isinstance(data, int):
        return data * 2
    elif isinstance(data, float):
        return data + 1.5
    elif isinstance(data, str):
        return data.upper()
    else:
        raise TypeError("Unsupported data type")
# Example of using the process_data function with different data types
print(process_data(10))          # Output: 20
print(process_data(3.14))       # Output: 4.64
print(process_data("hello"))    # Output: HELLO
# Example of function polymorphism with different data types
def display_info(data):
    if isinstance(data, list):
        print("List contents:")
        for item in data:
            print(item)
    elif isinstance(data, dict):
        print("Dictionary contents:")
        for key, value in data.items():
            print(f"{key}: {value}")
    elif isinstance(data, set):
        print("Set contents:")
        for item in data:
            print(item)
    else:
        print("Unsupported data type")
# Example of using the display_info function with different data types
display_info([1, 2, 3])          # List contents: 1, 2, 3
display_info({"name": "Alice", "age": 30})  # Dictionary contents: name: Alice, age: 30
display_info({1, 2, 3})          # Set contents: 1, 2, 3
# Example of function polymorphism with different data types
def calculate_discount(price, discount):
    if isinstance(price, int) or isinstance(price, float):
        return price * (1 - discount)
    elif isinstance(price, str):
        return f"Discounted price: {price} with {discount*100}% off"
    else:
        raise TypeError("Unsupported data type for price")
# Example of using the calculate_discount function with different data types
print(calculate_discount(100, 0.2))          # Output: 80.0
print(calculate_discount(50.5, 0.1))        # Output: 45.45
print(calculate_discount("100 USD", 0.15))  # Output: Discounted price: 100 USD with 15.0% off

#string
#For strings len() returns the number of characters:
print(len("Hello, World!"))  # Output: 13
# list
# For lists len() returns the number of items in the list:
print(len([1, 2, 3, 4, 5]))  # Output: 5
# tuple
# For tuples len() returns the number of items in the tuple:
print(len((1, 2, 3)))  # Output: 3
# dictionary
# For dictionaries len() returns the number of key-value pairs:
print(len({"name": "Alice", "age": 30}))  # Output: 2
# set
# For sets len() returns the number of unique items in the set:
print(len({1, 2, 3, 4, 5}))  # Output: 5

#class polymorphism
#Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
#For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
class Car:
    def move(self):
        return "The car is driving on the road."
class Boat:
    def move(self):
        return "The boat is sailing on the water."
class Plane:
    def move(self):
        return "The plane is flying in the sky."
# We can create a function that takes an object and calls its move method, regardless of the object's class:

def make_it_move(vehicle):
    print(vehicle.move())
# Example of using the make_it_move function with different vehicle types
car = Car()
boat = Boat()
plane = Plane()
make_it_move(car)   # Output: The car is driving on the road.
make_it_move(boat)  # Output: The boat is sailing on the water.
make_it_move(plane) # Output: The plane is flying in the sky.
# This is an example of polymorphism in action, where the same function can work with different types of objects.
class Car:
 def __init__(self, brand, model):
    self.brand = brand
    self.model = model
 def move(self):
        print("The car is driving on the road.")
class Boat:
 def __init__(self, brand, model):
    self.brand = brand
    self.model = model
 def move(self):
            print("The boat is sailing on the water.")
class Plane:
 def __init__(self, brand, model):
    self.brand = brand
    self.model = model
 def move(self):
        print("The plane is flying in the sky.")
car1 = Car("Toyota", "Camry")
boat1 = Boat("Yamaha", "242X")
plane1 = Plane("Boeing", "747")

for vehicle in (car1, boat1, plane1):
   print(f"{vehicle.brand} {vehicle.model}: ", end="")
vehicle.move()

#inheritance class polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


    

    



    


