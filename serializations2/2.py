import json

info = {
    'personal_data': {
        'name': 'Sai',
        'age': 22,
        'major': 'CSE',
        'physical_features': {
            'color': {'eye': 'brown', 'hair': 'black'},
            'height': "5'6"
        }
    },
    'other': {
        'favorite_colors': ['black', 'white', 'red '],
        'interested_in': ['social media', 'coding', 'content creation', 'music', 'books']
    }
}

print("Serializing to a string.")
string = json.dumps(info)

print(type(string))
print("\n")

print("Deserializing into a Python object.")
converted_info = json.loads(string)

print(type(converted_info))
