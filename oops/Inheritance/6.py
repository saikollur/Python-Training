class Company:
    def __init__(self, name):
        self.name = name
class Department(Company):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
class Employee(Department):
    def __init__(self,name,department,employeeName):
        super().__init__(name,department)
        self.employeeName = employeeName
    def display(self):
        print("Company Name  :", self.name)
        print("Department    :", self.department)
        print("Employee Name :", self.employeeName)
e = Employee("Intellibotics", "Zigma", "Sai Krishna")
e.display()  
