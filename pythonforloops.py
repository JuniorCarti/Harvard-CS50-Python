#Python For Loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#For loops in Python are control flow statements that allow you to repeatedly execute 
#a block of code for each item in a sequence (like lists, tuples, strings, etc.). 
# They follow this basic syntax:
#for item in iterable:
    # code to execute
#Core Components
#1. The Iterable
#Any Python object capable of returning its members one at a time:
"""Lists: [1, 2, 3]
Strings: "Hello"
Tuples: (1, 2, 3)
Dictionaries: {'a': 1, 'b': 2}
Sets: {1, 2, 3}
Range objects: range(5)
File objects
Generators"""
"""2. The Iterator Protocol
Python's for loops work through the iterator protocol:
Calls iter() on the iterable to get an iterator
Repeatedly calls next() on the iterator
Stops when StopIteration is raised"""

#1. Looping through a sequence
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

#2. Looping a specific number of times
for i in range(3):  # 0, 1, 2
    print("Hello")
#3. Looping with index and value
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
#4. Looping through dictionary items
person = {'name': 'John', 'age': 30}
for key, value in person.items():
    print(key, value)

#Advanced For Loop Techniques
#1. Nested Loops
for i in range(3):
    for j in range(2):
        print(i, j)
#2. Loop Control Statements
#break: Exit the loop
#continue: Skip to next iteration
#else: Execute if loop completes normally
for num in range(10):
    if num == 5:
        break
    print(num)
else:
    print("Loop completed")

#3. Zip for parallel iteration
names = ['Alice: ', 'Bob: ']
ages = [22, 30]
for name, age in zip(names, ages):
    print(name, age)

#4. List Comprehensions (compact loops)
squares = [x**2 for x in range(10)]

#1. Data Processing Pipeline (ETL)
## Extract raw data from multiple sources
"""raw_data_sources = [
    'sales_2025.csv',
    'inventory.db',
    'customer_api.json'
]

processed_data = []

# Transform and clean data
for source in raw_data_sources:
    if source.endswith('.csv'):
        # CSV processing logic
        with open(source) as f:
            data = process_csv(f) # type: ignore
    elif source.endswith('.db'):
        # Database processing
        data = query_database(source) # type: ignore
    else:
        # API processing
        data = fetch_api_data(source) # type: ignore
    
    # Clean data
    cleaned = clean_data(data) # type: ignore
    processed_data.append(cleaned)

# Load to data warehouse
for dataset in processed_data:
    load_to_warehouse(dataset) # type: ignore

#2. Automated Report Generation

# Generate departmental reports
departments = {
    'Sales': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Marketing': ['Campaign1', 'Campaign2'],
    'Engineering': ['Frontend', 'Backend']
}

for dept, projects in departments.items():
    print(f"\nGenerating {dept} Report:")
    print("=" * 30)
    
    total_hours = 0
    for project in projects:
        hours = get_project_hours(dept, project)
        total_hours += hours
        print(f"{project}: {hours} hours")
    
    print(f"\nTotal {dept} hours: {total_hours}")
    generate_pie_chart(dept, projects)
    send_email_report(dept)

#3. Web Scraping with Error Handling
import requests
from bs4 import BeautifulSoup

urls = [
    'https://example.com/products',
    'https://example.com/services',
    'https://example.com/about'
]

product_data = []

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract product cards
        for card in soup.select('.product-card'):
            name = card.select_one('.name').text.strip()
            price = card.select_one('.price').text.strip()
            rating = card.select_one('.rating')['data-value']
            
            product_data.append({
                'name': name,
                'price': price,
                'rating': rating,
                'source_url': url
            })
            
    except requests.exceptions.RequestException as e:
        print(f"Failed to process {url}: {str(e)}")
        continue
        
    except Exception as e:
        print(f"Unexpected error processing {url}: {str(e)}")
        continue

# Save to database
for product in product_data:
    save_to_database(product)


#Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String
for x in "banana":
  print(x)

#The break Statement
#With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#The continue Statement
#With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)"""

"""The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, 
starting from 0 by default, and increments by 1 (by default), and ends at a specified number."""


#Using the start parameter:
for x in range(2, 6):
  print(x)

#The range() function defaults to increment the sequence by 1, 
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

#Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# The else block will NOT be executed if the loop is stopped by a break statement.
#Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")