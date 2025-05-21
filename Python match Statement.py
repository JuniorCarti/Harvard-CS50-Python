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