#python json
# https://docs.python.org/3/library/json.html
import json
# json.dumps() converts a Python object into a JSON string
def json_dumps_example():
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    json_string = json.dumps(data)
    print("JSON String:", json_string)
# json.loads() converts a JSON string into a Python object
def json_loads_example():
    json_string = '{"name": "John", "age": 30, "city": "New York"}'
    data = json.loads(json_string)
    print("Python Object:", data)
# json.dump() writes a Python object to a file in JSON format
def json_dump_example():
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    with open('data.json', 'w') as file:
        json.dump(data, file)
    print("Data written to data.json")
# json.load() reads a JSON file and converts it into a Python object
def json_load_example():
    with open('data.json', 'r') as file:
        data = json.load(file)
    print("Data loaded from data.json:", data)
# Example usage
if __name__ == "__main__":
    json_dumps_example()
    json_loads_example()
    json_dump_example()
    json_load_example()
    
    # Additional examples
    # Pretty printing JSON
    data = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "children": ["Ann", "Billy"]
    }
    pretty_json_string = json.dumps(data, indent=4)
    print("Pretty JSON String:\n", pretty_json_string)
    
    # Sorting keys in JSON
    sorted_json_string = json.dumps(data, sort_keys=True, indent=4)
    print("Sorted JSON String:\n", sorted_json_string)
    # Handling non-serializable objects
    class CustomObject:
        def __init__(self, name):
            self.name = name
    def custom_object_serializer(obj):
        if isinstance(obj, CustomObject):
            return {"CustomObject": obj.name}
        raise TypeError(f"Type {type(obj)} not serializable")
    custom_obj = CustomObject("Example")
    custom_json_string = json.dumps(custom_obj, default=custom_object_serializer)
    print("Custom JSON String:", custom_json_string)

# Handling JSON with complex data types
def complex_data_example():
    data = {
        "name": "John",
        "age": 30,
        "is_active": True,
        "balance": 1234.56,
        "tags": ["developer", "python", "json"],
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "zip": "10001"
        }
    }
    json_string = json.dumps(data, indent=4)
    print("Complex JSON String:\n", json_string)
if __name__ == "__main__":
    complex_data_example()

#json is a syntax for storing and exchanging data
# It is language-independent, but uses conventions that are familiar to programmers of the C family of languages, 
# which includes C, C++, C#, Java, JavaScript, Perl, Python, and many others.
# JSON is often used when data is sent from a server to a web page.
# It is easy for humans to read and write, and easy for machines to parse and generate.
#Parse JSON - Convert from JSON to Python
#Stringify JSON - Convert from Python to JSON
#some JSON data
json_data = '{"name": "John", "age": 30, "city": "New York"}'
#parse JSON data
parsed_data = json.loads(json_data)
#access data
print("Name:", parsed_data['name'])
print("Age:", parsed_data['age'])
print("City:", parsed_data['city'])
# Stringify JSON data
json_string = json.dumps(parsed_data)
print("JSON String:", json_string)
# json.dumps() is used to convert a Python object into a JSON string
# json.loads() is used to parse a JSON string into a Python object
# json.dump() writes a Python object to a file in JSON format
# json.load() reads a JSON file and converts it into a Python object
# json.dumps() is used to convert a Python object into a JSON string
#convert Python object to JSON
python_object = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
}
json_string = json.dumps(python_object)
print("Converted JSON String:", json_string)




    


