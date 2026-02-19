class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Amount {amount} successfully credited!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Amount {amount} successfully debited!")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


account = BankAccount(10000)
account.deposit(1000)
account.withdraw(2000)
print("Available Balance :", account.get_balance())
