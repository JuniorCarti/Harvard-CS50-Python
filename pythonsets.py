myset = {"Benz", "Rav4", "Volvo", "AudiR3 Sportback"}
#Sets are used to store multiple items in a single variable.
#Set is one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
#A set is a collection which is unordered, unchangeable*, and unindexed.
#Sets are written with curly brackets.
print(myset)
#Note: Sets are unordered, so you cannot be sure in which order the items will appear.
#Set Items
#Set items are unordered, unchangeable, and do not allow duplicate values.
#Unordered
#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can remove items and add new items.
#Duplicates Not Allowed
#Sets cannot have two items with the same value.
cars = {"Benz", "Rav4", "Volvo", "AudiR3 Sportback", "Benz"}
print(cars)
#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
#True and 1 is considered the same value:
cars = {"Benz", "Rav4", "Volvo", "AudiR3 Sportback", "Benz", True, 1, 2}
print(cars)

#Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
cars = {"Benz", "Rav4", "Volvo", "AudiR3 Sportback", "Benz", False, 0, 2}
print(cars)

#Get the Length of a Set
#To determine how many items a set has, use the len() function.
cars = {"Benz", "Rav4", "Volvo", "AudiR3 Sportback", "Benz", False, 0, 2}
print(len(cars))

#Set Items - Data Types
#Set items can be of any data type:
cars = {"Benz", "Rav4", "Volvo", "AudiR3 Sportback", "Benz"} #str
numbers = {1, 2, 3, 4}
bools = {True, False, False, True}
floats = {2.4, 4.6, 8.0, 10.4}

print(type(cars))
print(type(numbers))
print(type(bools))
print(type(floats))

#A set can contain different data types:
#A set with strings, integers and boolean values:
different_data_types = {"Benz", "Rav4", "Volvo", True, False, 2.5, 5.5, 8.9, 1, 2, 3}
print(different_data_types)

#The set() Constructor
#It is also possible to use the set() constructor to make a set.
#Using the set() constructor to make a set:
fruits = set(("Apple", "Cherry", "Mango", "Beetroot"))
print(fruits)
#*Set items are unchangeable, but you can remove items and add new items.
#In Python, sets are unordered collections of unique elements. Since sets are unordered, 
#you cannot access items by index. However, there are several ways to access and manipulate set items efficiently.
#1. Iterating Over a Set
#The most common way to access items in a set is by iterating through it using a loop.
cars = {"Benz", "Rav4", "Volvo", "AudiR3 Sportback", "Benz"}
for car in cars:
    print(car)
#The items are printed in an arbitrary order:
#Sets do not maintain any specific order.
#The loop iterates over each item, regardless of their original order.

#2. Checking If an Item Exists
#Use the in keyword to check if an element is present in the set.
cars = {"Benz", "Rav4", "Volvo", "AudiR3 Sportback", "Benz"}
if "Benz" in cars:
    print("Car on Sale!!!!");
#The in keyword returns True if the item is present.
#This is efficient with sets due to their hash-based structure (average time complexity: O(1)).

#3. Accessing All Items at Once
#If you want to access all elements at once as a list, use the list() function.
cities = {"Nairobi", "Kisumu", "Nakuru", "Mombasa", "Kwale", "Nyeri"}
print(list(cities))
#Converts the set into a list, allowing you to access elements using indices.
#The order is still arbitrary because sets do not guarantee order.

#4. Using the set.pop() Method
#The pop() method removes and returns an arbitrary element from the set.
animals = {"cat", "dog", "elephant", "rhino"}
item = animals.pop()
print(f"Popped: {item}")
print("Remaining:", animals)
#The method removes a random element (not the first or last).
#If the set is empty, it raises a KeyError.
#animals = {}
#item = animals.pop()
#print(f"Popped: {item}")
#print("Remaining:", animals)

#5. Converting to List and Accessing by Index
#If you must access by index, convert the set to a list first.
colors = {"red", "green", "orange", "pink", "blue"}
colour_list = list(colors)
print(colour_list)
#access the index
print(colour_list[0])
#Conversion to a list allows indexed access.
#However the order might differ each time

#6. Unpacking the Set
#You can unpack a set into variables if you know the exact number of elements.
cities = {"Nairobi", "Kisumu", "Nakuru", "Mombasa", "Kwale", "Nyeri"}
city1, city2, city3, city4, city5, city6 = cities
print(city1, city2, city3, city4, city5, city6)