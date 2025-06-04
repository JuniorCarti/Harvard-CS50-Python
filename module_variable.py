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
