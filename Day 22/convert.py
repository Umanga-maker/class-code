import json
# python dictionary
data = {"name": "Alice", "age":30, "city": "New York"}

# Serialize into json
json_string = json.dumps(data)
print(json_string)