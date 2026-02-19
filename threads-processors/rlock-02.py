# A thread acquires the same lock multiple times using RLock.

import threading
import time

rlock = threading.RLock()

def recur(n):
    with rlock:
        print(f"Entering level - {n}")
        if n > 0:
            with rlock:
                recur(n - 1)
        print(f"Exiting level - {n}")

t1 = threading.Thread(target=recur, args=(5,))
t1.start()
