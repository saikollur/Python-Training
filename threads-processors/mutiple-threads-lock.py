# Multiple threads sharing access to update count

import threading
import time

count = 100
lock = threading.Lock()

def counter():
    global count
    with lock:
        if count > 0:
            count -= 1
            print(threading.current_thread().name, "count: ", count)
            
print("Intial count: ", count)

for i in range(4):
    t = threading.Thread(target = counter, name=f"Thread - {i+1}")
    t.start()

----------------------------------------
Output:

Intial count:  100
Thread - 1 count:  99
Thread - 2 count:  98
Thread - 3 count:  97
Thread - 4 count:  96
