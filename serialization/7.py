import json

try:
    with open('jsonFile.json', 'r') as file:
        string = file.read()

    details = json.loads(string)
    print("Valid JSON!")
    print(details)

except json.JSONDecodeError:
    print("Invalid JSON detected!")
    print("Handling it...")

    jsonF = {
        "name" : "PK",
        "profession" : "Actor",
        "age" : 55
    }

    with open('jsonFile.json', 'w') as file:
        json.dump(jsonF, file)
    
    with open('jsonFile.json', 'r') as file:
        string = json.load(file)

    print('\n',string)
    print("\nSuccessfully handled invalid JSON string")
