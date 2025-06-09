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