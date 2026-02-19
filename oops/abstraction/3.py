from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def interest_rate(self):
        pass
class savings(Bank):
    def interest_rate(self):
        return "The interest rate for savings ac is 5%"
class current(Bank):
    def interest_rate(self):
        return "The interest rate for current ac is 8%"

SA = savings()
CA = current()
print(SA.interest_rate())
print(CA.interest_rate())
