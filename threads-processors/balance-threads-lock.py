# Usage of LOCK to prevent invalid transactions

import threading

balance = 10000
lock = threading.Lock()

def withdraw(amount):
    with lock:
        global balance
        temp = balance
        if temp-amount < 0:
            print("Insufficient Balance. You have only -",balance)
        else:
            temp -= amount
            balance = temp
            print("Balance after withdrawal:", balance)

print("Intial Balance: ", balance)

t1 = threading.Thread(target=withdraw, args=(3000,))
t2 = threading.Thread(target=withdraw, args=(8000,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final balance:", balance)
----------------------------------------
Output: 

Intial Balance:  10000
Balance after withdrawal: 7000
Insufficient Balance. You have only - 7000
Final balance: 7000
