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