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
