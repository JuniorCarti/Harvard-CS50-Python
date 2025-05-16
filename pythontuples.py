#python tuples
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.
# Tuples are defined by enclosing the elements in parentheses ().
# Tuples can contain any type of data, including other tuples.
# Tuples are often used to return multiple values from a function.

mytuple = ("apple", "banana", "cherry")
print(mytuple)

#Create a Tuple:
# Creating a tuple
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)

Eldohub_courses = ("Networking and Cyber Security", "Full Stack Web", "Data Science", "Digital Literacy", "Graphic Design")
print(Eldohub_courses)


#Tuple with mixed data types

mixed_tuples = ("Apple", 1, "Banana", True, "House")
print(mixed_tuples)

#Nested tuples
nested_tuples = (("Apple", "Orange"), (1,2,4,5,6,7))
print(nested_tuples)

#single element tuple
single_element_tuple = (5,)
print(single_element_tuple)

#empty tuple
empty_tuple = ()
print(empty_tuple)

#tuple with strings
string_tuples = ('Apple', 'Cherry', 'Banana', 'Orange')
print(string_tuples)

#tuples allow duplicate values
duplicate_strings = ('apple', 'orange', 'apple', 'banana', 'mango', 'banana')
print(duplicate_strings)
print(len(duplicate_strings))

#tuple items data types; 
#tuple items can be of any data type
tuple_integer = (1,2,3,4,5,6,)
print(type(tuple_integer))
tuple_bool = (False, True, False, True)
tuple_float = (1.1, 4.5, 5.8)
tuple_string = ("Ridge", "Kim", "Dee", "Ray")

print(tuple_integer)
print(tuple_bool)
print(tuple_float)
print(tuple_string)

#a tuple with strings intergers and boolean values
tuple_mixed = (1, "apple", True, 2.5, "female")
print(tuple_mixed)

#knowing the type
tuple_integer = (1,2,3,4,5,6,)
print(type(tuple_integer))

#the tuple constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

tuple_constructor = tuple(('mercedes benz', 'Rav4', 'Audi', 'Bentley', 'Subaru'))
print(tuple_constructor)

#accessing tuples by index
#Indexing starts at 0 for the first item and -1 for the last item.
#Syntax: tuple[index]

cars = ("Benz", "Subaru", "Audi SportBack", "Toyota Hilux", "Prado 2025")
print(cars[0])
print(cars[1])
print(cars[2])
print(cars[3])
print(cars[-1])
print(cars[-3])

#If you access an index that does not exist, it raises an IndexError:
#print(cars[-6])

#slicing tuples
#Syntax: tuple[start:end:step]
#Slicing creates a new tuple from the specified range.
numbers = (1,2,3,4,5,6,7,8,9,10)
print(numbers[0:3])
print(numbers[1:4])
print(numbers[4:8])
print(numbers[:4])
print(numbers[4:])
print(numbers[::4]) ## Output: (1, 3, 5, 7, 9) (every fourth item)
print(numbers[4::])
print(numbers[::-1])

#negative slicing
print(numbers[-4:-1])

# Accessing Nested Tuples
#Tuples can contain other tuples (nested tuples). We access nested elements using multiple indices.
tuples_nested = (1, (1,2,3,4,5), ("Benz", "Audi", "Prado"), ("orange", "mango", "banana", "apple"))
print(tuples_nested[1])
print(tuples_nested[-1])
print(tuples_nested[3][-1])

#iterating through a tuple
#We can use a for loop to access all elements in a tuple.
colors = ('red', 'green', 'yellow', 'brown')
for color in colors:
    print(color)

countries = ("Kenya", "Tanzania", "Morrocco", "Tunisia", "South Africa", "Uganda")
for country in countries:
    print(countries)

#We can also access both index and value using enumerate():
for index, value in enumerate(countries):
    print(f"Index {index}: {value}")

for index, value in enumerate(colors):
    print(f"Index {index}: {value}")

#checking for existense of an item
counties = ('kisumu', 'nairobi', 'busia', 'nakuru', 'mombasa', 'kwale', 'naivasha')
print("machakos" in counties)
print("kisumu" in counties)
print("nairobi" in counties)
print("naivasha" in counties) 

#accessing tuple length
print(len(counties))

# Accessing Tuple Elements Using Indexing in Loops
#Access items using a for loop and index.

phones_brands = ('Samsung', 'Iphone 16', 'Tecno Spark4', 'Infinix')
for i in range(len(phones_brands)):
    print(f"Index {i}: {phones_brands[i]} ")

#accessing tuple elements using unpacking
coordinates = (10,20,30)
x,y,z = coordinates

print(x)
print(y)
print(z)

#accessing with a slice object
schools = (("Eldohub"), ("ALX"),  "Moringa", "Cyber Shujjaa", "Linux Foundations")
s = slice(0, 1, 2)
print(schools[s])

"""Indexing: Access specific elements using positive or negative indices.
Slicing: Extract a range of elements using start, stop, and step values.
Nested Tuples: Access nested elements using multiple indices.
Iterating: Loop through the tuple using for or enumerate().
Unpacking: Assign multiple elements to multiple variables in one statement.
Slice Object: Use slice() for more complex slicing."""

#✅ Updating Tuples in Python
#Tuples are immutable, meaning that once a tuple is created, 
#its elements cannot be modified, added, or removed directly. 
# However, there are some techniques to simulate updates.
#1. Convert Tuple to List and Update
"""The most common method to update a tuple is to:
Convert the tuple to a list.
Update the list.
Convert the list back to a tuple."""

names = ("kim", "Abby", "Sharon", "bella", "Frank", "Joyce")

#convert to list
name_list = list(names)
#print(name_list)

#update the list
name_list[1] = "ridge"

#convert back to tuple
names = tuple(name_list)
print(names)

#2. Adding Elements to a Tuple
#Since tuples are immutable, you cannot use append() or insert(). Instead, we can:
#Convert to a list, add the new element, and convert back to a tuple.
numbers = (1,2,3,4)
#Adding a single element
numbers = numbers + (5,)
print(numbers)
#Adding multiple elements
numbers = numbers + (5,6,7,8,9)
print(numbers)

#3. Removing Elements from a Tuple
#We cannot use methods like remove() or pop() directly. Instead, we:
#Convert the tuple to a list, remove the element, and convert back to a tuple.
fruits = ("apple", "banana", "cherry", "mango")
#convert to list
fruit_list = list(fruits)
#remove mango
fruit_list.remove("mango")
#convert back to a tuple
fruits = tuple(fruit_list)
print(fruits)

#python update tuples
#Change Tuple Values
"""Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple."""
#unpacking tuples
#2. Using the Asterisk (*) for Extended Unpacking
#You can use * to capture multiple elements into a list. This is known as extended unpacking.
numbers = (1,2,3,4,5)

a, *b, c = numbers
print(a)
print(b)
print(c)
#a takes the first value (1).
#b collects the middle values as a list ([2, 3, 4]).
#c takes the last value (5).

#3. Unpacking Nested Tuples
#If a tuple contains other tuples, you can unpack them in a nested structure.
#Nested tuple
nested = ('John', (25, "Engineer"), "NewYork")
print(nested)
print(len(nested))
name, (age, profession), city = nested

print(name)
print(age)
print(profession)
print(city)






