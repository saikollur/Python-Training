# Demonstrating DEADLOCK

import threading

lock = threading.Lock()

def task(c):
    with lock:
        if c > 0:
            with lock:
                print(c)
                task(c-1)

t1 = threading.Thread(target = task, args=(5, ))
t1.start()

#deadlock persists, so no output
