#Recursive task using RLock

import threading
import time

rlock = threading.RLock()

def recursive_task(count):
  with rlock:
    print("Count", count)
    if count > 0:
        recursive_task(count-1)

t = threading.Thread(target=recursive_task, args=(3,))
t.start()

----------------------------------------
Output:

Count 3
Count 2
Count 1
Count 0
