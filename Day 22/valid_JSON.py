import os
import json

file_path = "01_names.json"

if os.path.getsize(file_path) == 0:
    print("The file is empty.")
else:
    with open(file_path, "r") as f:
        data = json.load(f)
        print(data)


