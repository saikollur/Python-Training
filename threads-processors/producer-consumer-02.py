import threading
import time

condition = threading.Condition()
delivery_day = "wednesday"
flag = 0

def producer():
    global delivery_day
    global flag
    with condition:
        print("Delivery day is changed.")
        delivery_day = "Saturday"
        flag = 1
        condition.notify()

def consumer():
    global delivery_day
    global flag
    with condition:
        while flag != 1:
            condition.wait()
        print("Recieved update from delivery service.")
        print("The delivery day has been updated to,",delivery_day)

t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

t1.start()
time.sleep(1)
t2.start()

----------------------------------------
Output:

Delivery day is changed.
Recieved update from delivery service.
The delivery day has been updated to, Saturday
