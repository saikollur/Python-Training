class BankAccount:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin
        self.__authenticated = False

    def validate_pin(self, entered_pin):
        if entered_pin == self.__pin:
            self.__authenticated = True
            print("PIN verified successfully!")
        else:
            print("Incorrect PIN!")

    def deposit(self, amount):
        if not self.__authenticated:
            print("Please enter correct PIN first.")
            return

        self.__balance += amount
        print(f"Amount {amount} successfully credited!")

    def withdraw(self, amount):
        if not self.__authenticated:
            print("Please enter correct PIN first.")
            return

        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Amount {amount} successfully debited!")
        else:
            print("Insufficient funds")

    def get_balance(self):
        if not self.__authenticated:
            print("Please enter correct PIN first.")
            return
        return self.__balance

account = BankAccount(10000, 1234)

account.withdraw(2000)
account.validate_pin(1111)
account.validate_pin(1234)

account.deposit(1000)
account.withdraw(2000)
print("Available Balance :", account.get_balance())
