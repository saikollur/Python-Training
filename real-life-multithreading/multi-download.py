# A download manager must download 
# multiple files simultaneously. Write a program using threads.


import threading
import time

def downloads():
    print(f"{threading.current_thread().name}", "Downloading the file.")

for i in range(5):
    t1 = threading.Thread(target=downloads, name=(f"Thread {i+1}"))
    t1.start()
    t1.join()

print("Multiples files downloaded")

Thread 1 Downloading the file.
Thread 2 Downloading the file.
Thread 3 Downloading the file.
Thread 4 Downloading the file.
Thread 5 Downloading the file.
Multiples files downloaded
