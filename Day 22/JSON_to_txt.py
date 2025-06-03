import json

dic = {
    "name" : "John Smith",
    "Age" : 26, 
    "Id_num" : "12345678"
}

json_obj = json.dumps(dic, indent = 4)

with open("output.txt", "w") as f:
    f.write(json_obj)