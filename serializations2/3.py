import json

class obj:
    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept
    
data = obj("sai", 10593, "CSE")

student = {
    "name" : data.name,
    "id" : data.id,
    "dept" : data.dept,
}

with open('data.json', 'w') as f:
    json.dump(student, f)

with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(type(data))

