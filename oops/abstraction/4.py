from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return "Calculated salary for Fulltime Employee"

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return "Calculated salary for PartTime Employee"

FTE = FullTimeEmployee()
PTE = PartTimeEmployee()
print(FTE.calculate_salary())
print(PTE.calculate_salary())
