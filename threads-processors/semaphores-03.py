# Binary Semaphore

import threading
import time

count = 0
semaphore = threading.Semaphore(1)

def add():
    global count
    with semaphore:
        temp = count
        time.sleep(0.2)
        temp += 1
        count = temp
        print(threading.current_thread().name, "increased count by 1 so count is -", count)

for i in range(5):
    t = threading.Thread(target=add, name=f"Thread-{i+1}")
    t.start()

----------------------------------------
Output:

Thread-1 increased count by 1 so count is - 1
Thread-2 increased count by 1 so count is - 2
Thread-3 increased count by 1 so count is - 3
Thread-4 increased count by 1 so count is - 4
Thread-5 increased count by 1 so count is - 5
