from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class PermanentEmployee(Employee):
    def calculate_salary(self):
        print("Permanent Employee gets yearly rise.")


class ContractEmployee(Employee):
    def calculate_salary(self):
        print("Contract Employee gets no rise.")


employees = []
employees.append(PermanentEmployee())
employees.append(ContractEmployee())

for emp in employees:
    emp.calculate_salary()
