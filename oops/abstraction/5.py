from abc import ABC, abstractmethod

class School(ABC):
    @abstractmethod
    def employee_salary(self):
        pass
    @abstractmethod
    def student_fee(self):
        pass
    @abstractmethod
    def maintenance(self):
        pass
class Headmaster(School):
    def employee_salary(self):
        return "Credited ₹20000 to employee account"

sc = School()
hm = Headmaster()
print(sc.employee_salary())
print(hm.employee_salary())
