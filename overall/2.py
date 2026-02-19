import threading

lock = threading.Lock()

class Bank:
    def __init__(self, name):
        self.name = name
        self.__balance = 100000

    def deposit(self, amount):
        with lock:
            self.__balance += amount
            print(f'{amount} got credited into your account')
            print("Balance after deposit:", self.__balance)

    def withdraw(self, amount):
        with lock:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f'{amount} debited from your account')
            else:
                print("Insufficient balance")
            print("Balance after withdraw:", self.__balance)


ac = Bank("Sai Krishna")

t1 = threading.Thread(target=ac.deposit, args=(1000,))
t2 = threading.Thread(target=ac.withdraw, args=(2000,))

t1.start()
t2.start()

t1.join()
t2.join()
