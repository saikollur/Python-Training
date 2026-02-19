import threading
import time

condition = threading.Condition()
flag = 0

def producer():
    global flag
    with condition:
        print("Bike servicing started..")
        print("Bike service completed.")
        flag = 1
        condition.notify()

def consumer():
    global flag
    with condition:
        while flag != 1:
            condition.wait()
        
        print("Constumer picked up the bike.")
            
t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

t1.start()
time.sleep(1)
t2.start()

----------------------------------------
Output:

Bike servicing started..
Bike service completed.
Constumer picked up the bike.
