class BankAccount:
    def __init__(self, acNo, name, address, pincode, type):
        self.acNo = acNo
        self.name = name
        self.address = address
        self.pincode = pincode
        self.type = type

class SavingsAccount(BankAccount):
    def __init__(self,acNo,name,address,pincode,type,Balance):
        super().__init__(acNo,name,address,pincode,type)
        self.Balance = Balance
    def showBalance(self):
        print("Savings Account Balance: ", self.Balance)

class CurrentAccount(BankAccount):
    def __init__(self,acNo,name,address,pincode,type, Balance):
        super().__init__(acNo,name,address,pincode,type)
        self.Balance = Balance
    def showBalance(self):
        print("Current Account Balance: ", self.Balance)

ac1 = SavingsAccount("221810518", "Sai Krishna", "Tenali", "522201", "Savings", 100000)
ac2 = CurrentAccount("221809328", "Deepika", "Guntur", "522007", "Current", 2000000)

ac1.showBalance()
ac2.showBalance()
