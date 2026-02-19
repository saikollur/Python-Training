import json

with open('employee_Records.json', 'r') as file:
    data = file.read()

json_File = json.loads(data)

for item in json_File:
    salary = item['salary']
    annual_salary = salary * 12
    item['annual_salary'] = annual_salary

with open('employee_Records.json', 'w') as file:
    json.dump(json_File, file, indent=4)

with open('employee_Records.json', 'r') as file:
    print(file.read())
