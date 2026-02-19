#Limiting database connections using Semaphore

import threading
import time

n = int(input())
semaphore = threading.Semaphore(n)

def database():
    print(threading.current_thread().name, " Database is connected and accessed.")
    time.sleep(1)
    print(threading.current_thread().name, " Database connection is released.")

for i in range(10):
    t = threading.Thread(target = database, name=(f"Thread {i+1}"))
    t.start()

----------------------------------------
Output:

5
Thread 1  Database is connected and accessed.
Thread 2  Database is connected and accessed.
Thread 3  Database is connected and accessed.
Thread 4  Database is connected and accessed.
Thread 5  Database is connected and accessed.
Thread 6  Database is connected and accessed.
Thread 7  Database is connected and accessed.
Thread 8  Database is connected and accessed.
Thread 9  Database is connected and accessed.
Thread 10  Database is connected and accessed.
Thread 2  Database connection is released.
Thread 1  Database connection is released.
Thread 4  Database connection is released.
Thread 3  Database connection is released.
Thread 5  Database connection is released.
Thread 6  Database connection is released.
Thread 8  Database connection is released.
Thread 7  Database connection is released.
Thread 10  Database connection is released.
Thread 9  Database connection is released.
