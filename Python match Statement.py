#Python match Statement
#Basic sysntax
"""match subject:
    case pattern1:
        # handle pattern1
    case pattern2:
        # handle pattern2
    case _:
        # default case (like else)"""
#Simple Value Matching
#Works like a switch-case statement in other languages:
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown status"

print(http_status(200))  # "OK"
print(http_status(404))  # "Not Found"
print(http_status(999))  # "Unknown status"

#Pattern Matching with Types
def check_type(value):
    match value:
        case int():
            print(f"{value} is an integer")
        case float():
            print(f"{value} is a float")
        case str():
            print(f"{value} is a string")
        case _:
            print(f"Unknown type: {type(value)}")

check_type(42)      # "42 is an integer"
check_type(3.14)    # "3.14 is a float"
check_type("hello") # "hello is a string"
check_type([])      # "Unknown type: <class 'list'>"

#Sequence Patterns
#Match against lists, tuples, etc.:
def handle_command(command):
    match command.split():
        case ["quit"]:
            print("Quitting program")
        case ["load", filename]:
            print(f"Loading file: {filename}")
        case ["save", filename]:
            print(f"Saving to file: {filename}")
        case ["add", *items]:
            print(f"Adding items: {', '.join(items)}")
        case _:
            print("Unrecognized command")

handle_command("load data.txt")  # "Loading file: data.txt"
handle_command("add apples bananas")  # "Adding items: apples, bananas"
handle_command("random command")  # "Unrecognized command"

#Mapping Patterns
#Match against dictionaries:

def process_data(data):
    match data:
        case {"type": "person", "name": name, "age": int(age)}:
            print(f"Person: {name}, {age} years old")
        case {"type": "company", "name": name, "employees": employees}:
            print(f"Company: {name}, with {employees} employees")
        case _:
            print("Unknown Data Format")

# Calling the function with sample data
process_data({"type": "person", "name": "Ridge", "age": 25})
process_data({"type": "company", "name": "ACME", "employees": 100})
process_data({"type": "unknown", "info": "Something else"})

#Class Patterns
#Match against class attributes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def check_point(point):
    match point:
        case Point(x=0, y=0):
            print("Point is at the origin")
        case Point(x=0, y=y):
            print(f"Point is on Y axis at {y}")
        case Point(x=x, y=0):
            print(f"Point is on X axis at {x}")
        case Point(x=x, y=y):
            print(f"Point is at ({x}, {y})")
        case _:
            print("Not a point")

check_point(Point(0, 0))  # "Point is at the origin"
check_point(Point(0, 5))  # "Point is on Y axis at 5"
check_point(Point(3, 0))  # "Point is on X axis at 3"
check_point(Point(2, 3))  # "Point is at (2, 3)"

#Guards (Additional Conditions)
#Add conditions with if:
def check_number(value):
    match value:
        case int(x) if x > 0:
            print(f"Positive integer: {x}")
        case int(x) if x < 0:
            print(f"Negative integer: {x}")
        case float(x) if x > 0:
            print(f"Positive float: {x}")
        case float(x) if x < 0:
            print(f"Negative float: {x}")
        case 0:
            print("Zero")
        case _:
            print("Not a number")

check_number(42)     # "Positive integer: 42"
check_number(-3.14)  # "Negative float: -3.14"
check_number(0)      # "Zero"

#OR Patterns
#Match multiple patterns with |:
def check_color(color):
    match color:
        case "Red" | "Green" | "Blue":
            print("Primary RGB color")
        case "Yellow" | "Cyan" | "Magenta":
            print("Secondary color")
        case _:
            print("Not a basic color")
check_color("Red")
check_color("Yellow")
check_color("brown")

#1. Processing API Responses
def handle_response(response):
    match response:
        case {"status": 200, "data": data}:
            process_data(data)