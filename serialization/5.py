import json

class obj:
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

s1 = obj("sai", 22, "ACSE")

try:
    with open('studentDict.json', 'w') as f:
        json.dump(s1, f)
except TypeError as e:
    print("Serialization Error :", e)

    print("Converting object to dictionary...")

    student_Data = {
        'name' : s1.name,
        'age' : s1.age,
        'dept' : s1.dept
    }

    with open('studentDict.json', 'w') as f:
        json.dump(student_Data, f)

    print("Object successfully serialized!")
