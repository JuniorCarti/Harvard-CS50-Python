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