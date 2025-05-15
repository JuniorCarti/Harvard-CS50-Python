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


