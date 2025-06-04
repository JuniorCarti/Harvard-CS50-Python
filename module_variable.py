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
