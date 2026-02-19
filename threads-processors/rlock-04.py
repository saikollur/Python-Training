# Using RLock to prevent DEADLOCK

import threading

lock = threading.RLock()

def task(c):
    with lock:
        if c > 0:
            with lock:
                print(c)
                task(c-1)

t1 = threading.Thread(target = task, args=(5, ))
t1.start()

----------------------------------------
Output:

5
4
3
2
1
