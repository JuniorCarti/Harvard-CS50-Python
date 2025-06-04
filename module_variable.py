#module variable.py
# A variable created in a module is available in that module and can be accessed by importing the module.
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
# Example of a variable in a module
def get_person_info():
    return person1
# Example of using the module variable
def main_person():
    person_info = get_person_info()
    print("Person Info:", person_info)
if __name__ == "__main__":
    main_person()
# Import the module named module_variable and call the get_person_info function
import module_variable
print("Person Info:", module_variable.get_person_info())

#rename the module_variable.py to person_info.py
# Import module_variable as person_info
import module_variable as person_info
# Call the get_person_info function from the person_info module
print("Person Info:", person_info.get_person_info())

#Built-in Modules
# Python provides a rich set of built-in modules that you can use to perform various tasks.
#platform module
import platform
# Example of using the platform module to get system information
def get_system_info():
    return platform.system(), platform.release()
# Example of using the get_system_info function
def main_platform():
    system, release = get_system_info()
    print(f"System: {system}, Release: {release}")
if __name__ == "__main__":
    main_platform()
# datetime module
import datetime
# Example of using the datetime module to get the current date and time
def get_current_datetime():
    return datetime.datetime.now()
# Example of using the get_current_datetime function
def main_datetime():
    current_datetime = get_current_datetime()
    print(f"Current Date and Time: {current_datetime}")
if __name__ == "__main__":
    main_datetime()
# random module
import random
# Example of using the random module to generate a random number
def generate_random_number(start, end):
    return random.randint(start, end)
# Example of using the generate_random_number function
def main_random():
    random_number = generate_random_number(1, 100)
    print(f"Random Number: {random_number}")
if __name__ == "__main__":
    main_random()
# os module
import os
# Example of using the os module to get the current working directory
def get_current_directory():
    return os.getcwd()

