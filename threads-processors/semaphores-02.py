# Demostration of semaphores 

import threading
import time

semaphore = threading.Semaphore(3)

def task():
    with semaphore:
        print(threading.current_thread().name, "is in use.")
        time.sleep(1)
        print(threading.current_thread().name, "is free to use.")
for i in range(4):
    t = threading.Thread(target = task, name=(f"Printer - {i+1}"))
    t.start()

----------------------------------------
Output:

Printer - 1 is in use.
Printer - 2 is in use.
Printer - 3 is in use.
Printer - 2 is free to use.
Printer - 1 is free to use.
Printer - 4 is in use.
Printer - 3 is free to use.
Printer - 4 is free to use. 
