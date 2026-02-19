# A server must handle multiple client requests concurrently. 
# Write a program using threads to simulate handling multiple clients.

import threading
import time

n = int(input("Enter number of concurrent requests allowed: "))
sem= threading.Semaphore(n)

def database():
    with sem:
        print(f"{threading.current_thread().name} is accessing the database")
        time.sleep(2)
        print(f"{threading.current_thread().name} has finished accessing the database")

for i in range(n):
    t = threading.Thread(target = database, name = (f"Thread-{i+1}"))
    t.start()

Enter number of concurrent requests allowed: 5
Thread-1 is accessing the database
Thread-2 is accessing the database
Thread-3 is accessing the database
Thread-4 is accessing the database
Thread-5 is accessing the database
Thread-1 has finished accessing the database
Thread-2 has finished accessing the database
Thread-3 has finished accessing the database
Thread-4 has finished accessing the database
Thread-5 has finished accessing the database
