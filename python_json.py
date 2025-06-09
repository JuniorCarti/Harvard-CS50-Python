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
    
