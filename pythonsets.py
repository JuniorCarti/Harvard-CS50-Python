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