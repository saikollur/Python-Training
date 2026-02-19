import json

students = [
    {
        "name" : "sai",
        "age" : 22,
        "college" : "vignan"
    },
    {
        "name" : "tarun",
        "age" : 20,
        "college" : "vignan"
    },
    {
        "name" : "sasi",
        "age" : 21,
        "college" : "srm"
    },
    {
        "name" : "vydhu",
        "age" : 24,
        "college" : "KL"
    },
    {
        "name" : "pavan",
        "age" : 19,
        "college" : "vit"
    },
    {
        "name" : "arjun",
        "age" : 18,
        "college" : "bits"
    }
]

with open('list.json', 'w') as file:
    json.dump(students, file, indent = 4, sort_keys=True, ensure_ascii=False)

with open('list.json', 'r') as file:
    data = json.load(file)

for item in data:
    if item['age'] >= 18 and item['age'] <= 23:
        print(item)
