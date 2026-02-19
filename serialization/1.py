import json

student = {
        "name" : ['K. Sai Krishna', 'N. Tarun', 'M. Sasidhar'],
        "course" : ['AI&ML', 'BFA', 'BA'],
        "department" : ['ACSE', 'Arts', 'Finance']
    }

with open("students.json", "w") as f:
    json.dump(student, f)

with open("students.json", "r") as f:
    newStudents = json.load(f)
    newStudents["marks"] = [78, 98, 88]

with open("newStudents.json", "w") as f:
    json.dump(newStudents, f)

print(newStudents)
print(type(newStudents))
