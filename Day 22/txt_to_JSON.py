from ast import literal_eval
import json

with open("output.txt", 'r', encoding='utf8') as data:
    # Reading and sanitizing the content
    raw_content = data.read().replace('\r\n', '')
    # Safely evaluating the string structure
    data_structure = literal_eval(raw_content)

json_data = json.dumps(data_structure, ensure_ascii=False, indent=4)
print(json_data)