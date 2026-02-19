# A banking system must update account balance while 
# logging transactions at the same time. 
# Write a multithreading program for this scenario.


import threading
import time

event = threading.Event()

balance = 100000
logging = []

def withdrawal(amount):
    global balance
    temp = balance
    temp -= amount
    balance = temp
    print(f"Amount Available:",balance)
    event.set()

def loggings(amount):
    global balance
    event.wait()
    if amount <= balance:
        logging.append(amount)
    print(f"Logged balance.")

while True:
    amount = int(input("Enter amount to withdraw: "))
    if amount == 0:
        break
    t1 = threading.Thread(target=withdrawal, args=(amount,))
    t2 = threading.Thread(target=loggings, args=(amount,))
    t1.start()
    t2.start()

t1.join()
t2.join()

print("Transactions: ")
print(logging)

Enter amount to withdraw: 50
Amount Available: 98610
Logged balance.
Enter amount to withdraw: 1000
Amount Available: 97610
Logged balance.
Enter amount to withdraw: 2000
Amount Available: 95610
Logged balance.
Enter amount to withdraw: 0
Transactions: 
[1000, 300, 40, 50, 1000, 2000]
