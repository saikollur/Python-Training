# Using Semaphore to limit resources

import threading
import time

semaphore = threading.Semaphore(2)

def task():
    with semaphore:
        print(threading.current_thread().name, "is accessing the resource.")
        time.sleep(2)
        print(threading.current_thread().name, "is leaving the resource.")
for i in range(4):
    t = threading.Thread(target = task, name=(f"Thread - {i+1}"))
    t.start()

----------------------------------------
Output:

Thread - 1 is accessing the resource.
Thread - 2 is accessing the resource.
Thread - 1 is leaving the resource.
Thread - 2 is leaving the resource.
Thread - 3 is accessing the resource.
Thread - 4 is accessing the resource.
Thread - 4 is leaving the resource.
Thread - 3 is leaving the resource.
