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
#The order of unpacked variables is unpredictable.
#Will raise a ValueError if the number of elements does not match the variables.

#7. Accessing a Specific Item (Indirectly)
#If you need a specific element (e.g., the first one), convert the set to a list:
names = {"alice", "naomi", "njenga", "cynthia", "esperanza"}
first_item = next(iter(names))
print(first_item)
#iter(letters) creates an iterator.
#next() gets the first item from the iterator.
#still unpredictable in terms of order

#8. Random Access Using random.choice()
#Sets are unordered, but if you want to randomly pick an item:
import random

food = {"pizza", "chicken wings", "burger", "HotSauce"}
random_item = random.choice(list(food))
print(random_item)

#Converts the set to a list before using random.choice().
#Direct use of random.choice() on a set will raise a TypeError.

#9. Using next() and iter() Together
#A more memory-efficient way to get an element (without converting to a list):
nums = {10, 20, 30, 40, 50}
first = next(iter(nums))
print("First Item:", first)
#No list conversion needed, so it’s faster and uses less memory.
#Suitable when you only need a single item from the set.

#Key Takeaways
"""Sets do not support indexing or slicing because they are unordered.
Use a for loop to iterate over all items.
Use the in keyword to check for the presence of an item.
Use pop() to remove and access a random item.
Convert the set to a list for index-based access.
Use next(iter(set)) for efficient single-item access.
For random selection, use random.choice(list(set))."""

#✅ Adding Items to a Set in Python
#Sets in Python are mutable, meaning we can add and remove items. There are multiple ways to add items to a set:
#add() — Adds a single item.
#update() — Adds multiple items (from any iterable: list, tuple, set, etc.).
#1. Adding a Single Item with add()
#The add() method adds one element to the set.
cars = {"AudiR3 Sportback", "Range Rover", "Toyota Hilux", "Mercedes Benz", "Rav4"}
cars.add("Volvo")
print(cars)
print(len(cars))
#The add() method inserts the item, but its position is arbitrary due to the unordered nature of sets.
#If the item already exists in the set, it will not be added again since sets do not allow duplicates.

#2. Adding Multiple Items with update()
#The update() method can add multiple items from any iterable (list, tuple, set, etc.).
#Syntax: set_name.update(iterable)
cars = {"AudiR3 Sportback", "Range Rover", "Toyota Hilux", "Mercedes Benz", "Rav4"}
new_cars = ["Honda CRV", "Toyota Premio", "Toyota LandCruiser", "Mercedes Benz"] #example with list
cars.update(new_cars)
print(cars)
print(len(cars))
#The update() method only adds unique items.
#"Mercedes Benz" was already present, so it is not added again.

#example with tuple
fruits = {"apple", "orange", "pineapple", "beetroot", "mango"}
new_fruits = ("orange", "tomato", "guava", "avocado")
fruits.update(new_fruits)
print(fruits)
print(len(fruits))

#example with another set
laptops = {"Dell", "Apple", "HP", "Asus", "Lenovo"}
new_laptops = {"Huawei", "Microsoft", "Samsung"}
laptops.update(new_laptops)
print(laptops)
print(len(laptops))

#3. Adding Items from a String
#Strings are iterables, so each character is treated as a separate item:
names = {"alice", "jane", "sharon", "kevin", "ridge"}
names.update("brian, kim")
print(names)

#4. Adding Items Conditionally
# You can add items based on a condition using a loop:
numbers = {1, 2, 3}
for i in range(1, 6):
    if i not in numbers:
        numbers.add(i)

print(numbers)
#Only numbers not already in the set are added.
#5. Adding a Nested Set (Not Allowed)
#Sets are unhashable, so you cannot add a set as an item in another set. This will raise a TypeError.
set1 = {1, 2, 3}
set2 = {4, 5, 6}

# This will raise an error:
# set1.add(set2)
#If you want to add multiple items from another set, use update() instead:
set1.update(set2)
print(set1)

#6. Adding Immutable Objects (Like Tuples)
#Since tuples are immutable, they can be added to a set:
my_set = {1, 2, 3}
my_set.add((4, 5))
print(my_set)
#Tuples are hashable and can be added as a single item.
#7. Adding Complex Data Structures
#You can add nested data structures like tuples containing sets, but the sets must first be converted to frozensets:
my_set = {1, 2, 3}
nested = frozenset({4, 5})
my_set.add(nested)
print(my_set)

#frozenset is an immutable version of a set, making it hashable.
"""✅ Key Takeaways:
Use add() to insert a single item.
Use update() to insert multiple items (from lists, tuples, sets, strings, etc.).
Sets only accept immutable objects as items (e.g., integers, strings, tuples).
To add nested sets, convert them to frozenset."""

#Python - Remove Set Items
#To remove an item in a set, use the remove(), or the discard() method.
#remove method
laptops = {"Dell", "Apple", "HP", "Asus", "Lenovo"}
laptops.remove("Dell")
print(laptops)

#discard method
laptops = {"Dell", "Apple", "HP", "Asus", "Lenovo"}
laptops.discard("Apple")
print(laptops)

#pop method
#remove a random item  by using the pop method()
laptops = {"Dell", "Apple", "HP", "Asus", "Lenovo"}
new_laptops = laptops.pop()
print(new_laptops)
print(laptops)

#clear method
laptops = {"Dell", "Apple", "HP", "Asus", "Lenovo"}
laptops.clear()
print(laptops)

#the del keyword
#The del keyword will delete the set completely:
#laptops = {"Dell", "Apple", "HP", "Asus", "Lenovo"}
#del laptops
#print(laptops)
#you will get an error since the set has been deleted completely

#loop items
#You can loop through the set items by using a for loop:
laptops = {"Dell", "Apple", "HP", "Asus", "Lenovo"}
for Dell in laptops:
    print(Dell)

#✅ Joining Sets in Python
#In Python, we can join sets using various methods to combine their elements. The most common methods are:
"""Union (| or union() method)
Update (update() method)
section (& or intersection() method)
Symmetric Difference (^ or symmetric_difference() method)
Difference (- or difference() method)"""
#1. Union of Sets
#The union operation combines the elements of two or more sets and removes duplicates.
#Syntax:
#Using the union() method:
#set1.union(set2, set3, ...)

#Using the | operator:
#set1 | set2 | set3
set1 = {"AudiR3 Sportback", "Range Rover", "Toyota Hilux", "Mercedes Benz", "Rav4"}
set2 = {"Dell", "Apple", "HP", "Asus", "Lenovo"}
set3 = {"alice", "jane", "sharon", "kevin", "ridge"}

all_items = set1.union(set2, set3)
print("All the items are a union():", all_items)

#✅ Using the | Operator:
set1 = {"AudiR3 Sportback", "Range Rover", "Toyota Hilux", "Mercedes Benz", "Rav4"}
set2 = {"Dell", "Apple", "HP", "Asus", "Lenovo"}
set3 = {"alice", "jane", "sharon", "kevin", "ridge"}

# Using the | operator to join sets
all_items = set1 | set2 | set3

print("All the items using | operator:", all_items)
#The | operator performs a union operation between the sets, just like the union() method.
#It combines all unique elements from all the sets.
#The resulting set will contain all items from set1, set2, and set3, but without any duplicates.
#Both the | operator and the union() method perform the same operation, but the operator is shorter and often considered more readable.

#2. Update Method
#The update() method adds all unique elements from another set (or any iterable) to the original set.
#This modifies the original set in place.
#Syntax:
#set1.update(set2)
fruits = {"apple", "oranges", "mango"}
greens = {"kales",}
colors = {"red", "orange", "yellow",}

fruits.update(greens, colors)
print("After update():", fruits)

#3. Intersection of Sets
#The intersection operation returns a set containing only the common elements in both sets.
#Syntax:
#Using the intersection() method:
#set1.intersection(set2, set3, ...)
