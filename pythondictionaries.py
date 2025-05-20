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
        'E1001': {'name' : 'wireless Headphones', 'stock': 45, 'price': 154},
        'E1002': {'name' : 'Samsung 54inch TVs', 'stock': 50, 'price': 2300},
        'E1003': {'name' : 'Infinix Smartphones', 'stock': 15, 'price': 123}
    },
    'clothing': {
        'C1001': {'name': 'Khaki Trousers', 'stock': 123, 'price': 600},
        'C1002': {'name': 'Long-Sleeved Shirts', 'stock': 15, 'price': 120},
        'C1003': {'name': 'Denim Jeans', 'stock': 12, 'price': 130}
    },
    'furniture': {
        'F1001': {'name': 'Coffee Table', 'stock': 100, 'price': 1000},
        'F1002': {'name': 'Office Chairs', 'stock': 10, 'price': 1500}
    }
}

## Checking stock levels
def check_stock(category, product_id):
    product = inventory.get(category, {}) .get(product_id)
    if product:
        return f"{product['name']}: {product['stock']} in stock!"
    return "Product not found"

print(check_stock('furniture', 'F1001'))

## Processing an order
def process_order(category, product_id, quantity):
    if inventory[category][product_id]['stock'] >= quantity:
        inventory[category][product_id]['stock'] -= quantity
        total = inventory[category][product_id]['price'] * quantity
        return f"Order Processed. Total: ${total:.2f}"
    return "Insufficient Stock"

print(process_order('clothing', 'C1001', 57))


#Corrected Multi-Order Processing Solution


def process_multi_orders(*orders):
    #Process multiple orders and return results for each"""
    results = []
    for order in orders:
        if len(order) != 3:
            results.append(f"Invalid order format: {order}")
            continue
            
        category, product_id, quantity = order
        product = inventory.get(category, {}).get(product_id)
        
        if not product:
            results.append(f"Product {product_id} not found in {category}")
        elif product['stock'] >= quantity:
            inventory[category][product_id]['stock'] -= quantity
            total = product['price'] * quantity
            results.append(f"Order processed: {quantity}x {product['name']} - Total: ${total:.2f}")
        else:
            results.append(f"Insufficient stock for {product['name']} (requested: {quantity}, available: {product['stock']})")
    
    return "\n".join(results)

# Example usage with multiple orders
print(process_multi_orders(
    ('clothing', 'C1001', 57),
    ('furniture', 'F1001', 45),
    ('electronics', 'E1002', 10),
))

#API Response Processing
#Scenario: Working with JSON data from web APIs.
weather_data = {
    'location': {
        'city': 'Nairobi',
        'country': 'Kenya',
        'coordinates': {'lat': 40.71, 'long': -74.01}
    },
    'current': {
        'temp_c': 22.5,
        'temp_f': 72.4,
        'condition': {
            'text': 'Partly Cloudy',
            'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png',
            'code': 1003
        },
    'Other details':{
         'wind_kph': 15.2,
         'wind_mph': 3.8,
         'humidity': 65,
         'wind_dir': 'SW',
         'cloud': 75,
         'feelslike_c': 9.5,
         'feelslike_f': 49.2,
    }
    },
    'forecast': {
        'forecast_day': [
            {
                'date': '2025-05-20',
                'day': {
                    'maxtemp_c': 24.3,
                    'mintemp_c': 18.7,
                    'daily_chance_of_rain': 40
                }
            },
            {
                'date': '2025-05-21',
                'day': {
                    'maxtemp_c': 21.8,
                    'mintemp_c': 16.2,
                    'daily_chance_of_rain': 70
            }
            }
        ]
    }
}
#extracting relevant information
def format_weather_report(data):
    report = {
        'location': f"{data['location']['city'], {data['location']['country']}}",
        'current_temp': f"{data['current']['temp_c']} °C ({data['current']['temp_f']} °F)",
        'condition': f"{data ['current']['condition']['text']}",
        'other details': f"{data['wind_kph']['himidity']['cloud']}",
        'forecast': []
    }

    for day in data['forecast']['forecast_day']:
        report['forecast'].append({
            'date': day['date'],
            'high': day['day']['maxtemp_c'],
            'low': day['day']['mintemp_c'],
            'rain_chance': day['day']['daily_chance_of_rain']
        })
        return report
    print(format_weather_report(weather_data))


    
gradebook = {
    'math': {
        'Alice': [92, 85, 94],
        'Bob': [78, 82, 80],
        'Charlie': [88, 91, 95]
    },
    'science': {
        'Alice': [95, 89],
        'Bob': [76, 84, 82, 80],
        'Charlie': [92, 94]
    },
    'history': {
        'Alice': [87, 91],
        'Bob': [90, 85],
        'Charlie': [78, 82, 85]
    }
}

# Calculating average grades
def calculate_averages():
    averages = {}
    for subject, students in gradebook.items():
        subject_averages = {}
        for student, grades in students.items():
            avg = sum(grades) / len(grades)
            subject_averages[student] = round(avg, 1)
        averages[subject] = subject_averages
    return averages

# Adding a new assignment
def add_assignment(subject, scores):
    for student, grade in scores.items():
        if student in gradebook[subject]:
            gradebook[subject][student].append(grade)

# Usage
print("Math averages:", calculate_averages()['math'])
# Output might be: {'Alice': 90.3, 'Bob': 80.0, 'Charlie': 91.3}

add_assignment('science', {'Alice': 93, 'Bob': 79, 'Charlie': 96})
print("Updated science grades:", gradebook['science'])


#Basic Dictionary Modification
#1. Changing Values
person = {"name": "Alice", "age": 25, "city": "New York"}
# Change value using key
person['age'] = 26
print(person)