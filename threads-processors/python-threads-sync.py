# ** Demonstrating Race Condition **

import threading
import time

balance = 10000

def withdraw(amount):
    global balance
    temp = balance
    time.sleep(0.2)
    temp -= amount
    balance = temp
    print("Balance after withdrawal:", balance)

t1 = threading.Thread(target=withdraw, args=(3000,))
t2 = threading.Thread(target=withdraw, args=(8000,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final balance:", balance)

----------------------------------------
Output: 

Balance after withdrawal: 7000
Balance after withdrawal: 2000
Final balance: 2000
