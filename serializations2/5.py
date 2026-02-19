import json

string = 123456

try:
    data = json.loads(string)
    print("Valid JSON string")
    print(string)
except (json.JSONDecodeError , TypeError):
    print("Invalid JSON File")
    print("Fixing it.")

    modify = '"This is a string"'
    obj = json.loads(modify)
    
    print("Printing parts of the JSON String :", obj[5],"&",obj[6])
    print(type(obj))
