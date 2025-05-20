thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values:

print(thisdict)
#Dictionary Items
#Dictionary items are ordered, changeable, and do not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
print(thisdict["brand"])

#Duplicates Not Allowed
#Dictionaries cannot have two items with the same key:
#Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2023
}
#Dictionary Length
#To determine how many items a dictionary has, use the len() function:
print(len(thisdict))

#Dictionary Items - Data Types
#The values in dictionary items can be of any data type:
#String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))

#The dict() Constructor
#It is also possible to use the dict() constructor to make a dictionary.
#Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Basic Dictionary Access
#The simplest way to access a dictionary value is by using square bracket notation with the key.
my_dict = {'name': 'Alice', 'age': 35, 'occupation': 'nurse', 'town': 'eldoret', 'years of experience': 15}
#accessing values
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["occupation"])
print(my_dict["years of experience"])

#If you try to access a key that doesn't exist, Python raises a KeyError:
# This will raise KeyError
#print(my_dict['salary'])

#Access Methods
#1. get method()
#The get() method is a safer way to access dictionary values as it returns None 
#(or a default value you specify) if the key doesn't exist.