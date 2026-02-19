class Employee:
    def __init__(self, salary):
        self.__salary = salary
    def updateSalary(self, update):
        self.__salary += update
        print("Your salary got a updated.")
    def getSalary(self):
        return self.__salary

employee = Employee(100000)
employee.updateSalary(1000)
print("Employee salary:", employee.getSalary())
