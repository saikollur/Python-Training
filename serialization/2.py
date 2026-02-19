import json

data = {
    "students": [
        {
            "name": "Sai Krishna",
            "details": {
                "course": "AI&ML",
                "marks": [78, 85, 90]
            }
        },
        {
            "name": "Tarun",
            "details": {
                "course": "BFA",
                "marks": [88, 92, 80]
            }
        }
    ]
}

string = json.dumps(data, indent = 4)

with open('reconstruct.json', 'w') as file:
    file.write(string)

with open('reconstruct.json', 'r') as file:
    dict = file.read()

reconstructed = json.loads(dict)

print(reconstructed)
print(type(reconstructed))
