# mock_api_tester.py

def process_data(data):
    match data:
        case {"type": "person", "name": name, "age": int(age)}:
            print(f"Person: {name}, {age} years old")
        case {"type": "company", "name": name, "employees": employees}:
            print(f"Company: {name}, with {employees} employees")
        case [{"type": "person", "name": name, "age": int(age)} as person, *rest]:
            print("Person list:")
            print(f"- {name}, {age} years old")
            for item in rest:
                process_data(item)  # Recursive call
        case _:
            print("Unknown Data Format")


def handle_response(response):
    match response:
        case {"status": 200, "data": data}:
            print("✅ 200 OK")
            process_data(data)
        case {"status": 201, "message": msg}:
            print(f"✅ 201 Created: {msg}")
        case {"status": 404}:
            print("❌ 404 Not Found")
        case {"status": 500, "error": error}:
            print(f"🔥 500 Server Error: {error}")
        case {"status": code} if 400 <= code < 500:
            print(f"⚠️ Client Error: {code}")
        case {"status": code} if 500 <= code < 600:
            print(f"🔥 Server Error: {code}")
        case _:
            print("❓ Invalid response format")


def test_api_responses():
    responses = [
        {"status": 200, "data": {"type": "person", "name": "Ridge", "age": 25}},
        {"status": 200, "data": {"type": "company", "name": "ACME", "employees": 100}},
        {"status": 201, "message": "Resource created successfully"},
        {"status": 200, "data": [
            {"type": "person", "name": "Alice", "age": 30},
            {"type": "person", "name": "Bob", "age": 22}
        ]},
        {"status": 403},
        {"status": 500, "error": "Database unreachable"},
        {"message": "Missing status key"}
    ]

    print("\n📦 Mock API Response Tester\n----------------------------")
    for i, response in enumerate(responses, 1):
        print(f"\n🔄 Test Case {i}")
        handle_response(response)


if __name__ == "__main__":
    test_api_responses()
