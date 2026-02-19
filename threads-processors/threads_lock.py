# Usage of LOCK to prevent race condition


import threading
import time

balance = 10000
lock = threading.Lock()

def withdrawal(amount):
    with lock:
        global balance
        temp = balance
        temp -= amount
        balance = temp
        print("Balance after withdraw: ", balance)

print("Intial Balance: ", balance)

t1 = threading.Thread(target=withdrawal, args=(3000,))
t2 = threading.Thread(target=withdrawal, args=(5000,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final balance:", balance)

----------------------------------------
Output:

Intial Balance:  10000
Balance after withdraw:  7000
Balance after withdraw:  2000
Final balance: 2000
