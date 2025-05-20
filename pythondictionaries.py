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
print(my_dict.get('name'))
print(my_dict.get('salary'))
print(my_dict.get('age'))
print(my_dict.get('occupation'))
print(my_dict.get('years of experience'))

#2. keys() method
#Returns a view object containing the dictionary's keys.
keys = my_dict.keys()
print(keys)
print(list(keys))

#3. values() method
#Returns a view object containing the dictionary's values.
values = my_dict.values()
print(values)
print(list(values))

#4. items() method
#Returns a view object containing key-value pairs as tuples.
items = my_dict.items()
print(items)
print(list(items)) #Convert to list of tuples

#Checking Key Existence
#You can check if a key exists in a dictionary using the in keyword.
print('name' in my_dict)
print('age' in my_dict)
print('salary ' in my_dict)
print('Alice' in my_dict) # Output: False (checks keys, not values)

#Access Patterns
#Direct Access
#As shown earlier, you can access values directly using keys.
person = {
    'first_name': 'John',
    'last_name': 'Ridge',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'SQL'],
    'school': ('PLP Academy')
    
}

print(person['first_name'])             # Output: John
print(person['skills'][1])               # Output: JavaScript (access list within dict)
print(person.get("school"))


library = {
    'books': ('Python', 'Javascript', 'Java'),
    'borrowed_books': ['Python', 'Java'],
    'returned_books': ['Java']
}

print(library.get("books"))
print(library.get("returned_books"))

#loop access
#You can iterate through dictionaries in several ways:
# Loop through keys
for key in person:
    print(key, person[key])

for key in person:
    print(key, person[key])

# Equivalent to:
for key in person.keys():
    print(key, person[key])

# Loop through values
for value in person.values():
    print(value)

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

#dictionary comprehension
#You can create new dictionaries by processing existing ones.

# Create a dictionary with string lengths
words = ['apple', 'banana', 'cherry']
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}

# Filter dictionary
ages = {'John': 25, 'Alice': 30, 'Bob': 22}
adults = {name: age for name, age in ages.items() if age >= 25}
print(adults)        # Output: {'John': 25, 'Alice': 30}

#Nested Dictionary Access
#Dictionaries can contain other dictionaries, requiring nested access.
company = {
    'name': 'TechCorp',
    'departments': {
        'engineering': {
            'manager': 'Alice',
            'employees': 50
        },
        'marketing': {
            'manager': 'Bob',
            'employees': 20
        }
    }
}

# Access nested values
print(company['departments']['engineering']['manager'])  # Output: Alice
print(company.get('departments', {}).get('sales', {}).get('manager', 'No department'))  # Output: No department

#For deeply nested dictionaries, you might want to use a helper function:
def deep_get(dictionary, *keys, default=None):
    for key in keys:
        try:
            dictionary = dictionary[key]
        except (KeyError, TypeError):
            return default
    return dictionary

print(deep_get(company, 'departments', 'engineering', 'manager'))  # Output: Alice
print(deep_get(company, 'departments', 'sales', 'manager', default='Not found'))  # Output: Not found


#Practical examples
#Example 1: Counting word frequencies
def word_count(text):
    words = text.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

text = "apple banana apple cherry banana apple"
print(word_count(text))
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}

#Example 2: Merging dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}


merged = {**dict1, **dict2}
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Alternative
merged = dict1.copy()
merged.update(dict2)

#Example 3: Inverting a dictionary
original = {'a': 1, 'b': 2, 'c': 1}
inverted = {}

for key, value in original.items():
    inverted.setdefault(value, []).append(key)

print(inverted)  # Output: {1: ['a', 'c'], 2: ['b']}

#Example 4: Dictionary as switch-case alternative
def dispatch(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y
    }.get(operator, lambda: None)()

print(dispatch('add', 5, 3))  # Output: 8
print(dispatch('pow', 2, 3))  # Output: None


#1. User Profile Management
#Scenario: Storing and accessing user information in a web application.

#creating a user profile manangement
user = {
    'id': 'ui12345',
    'username' : 'Software Developer',
    'personal_info': {
        'name': 'Ridge Junior',
        'age':  '32',
        'location': 'Eldoret',
    },
    'account status': 'active',
    'prefernces': {
        'theme': 'dark',
        'notifications': 'enabled',
        'language': 'English',
    },
    'last_login': '2025-05-20T12:48PM'
}

#accessing user nested information
print(f"Welcome Back, {user['personal_info']['name']} !!")

#checking notification preference
if user['prefernces']['notifications']:
    print("You have notifications enabled")

#updating user status
user['account status'] = 'Premium'
print(f"You are now a, {user['account status']} user!")


#2. Inventory Management System
#Scenario: Tracking products in an e-commerce warehouse.

inventory = {
    'electronics': {
        'E1001': {'name' : 'wireless Headphones', 'stock': 45, 'price': '154.65usd'},
        'E1002': {'name' : 'Samsung 54inch TVs', 'stock': 50, 'price': '2300usd'},
        'E1003': {'name' : 'Infinix Smartphones', 'stock': 15, 'price': '123usd'}
    }
}