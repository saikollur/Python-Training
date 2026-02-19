import threading
import time

event = threading.Event()

def firstEvent():
    print("First event is executing.")
    event.set()

def secondEvent():
    print("Second event is waiting for signal.")
    event.wait()
    print("Signal receieved.. Second event is executing.")

t1 = threading.Thread(target=secondEvent)
t2 = threading.Thread(target=firstEvent)

t1.start()
t2.start()

----------------------------------------
Output:

Second event is waiting for signal.
First event is executing.
Signal receieved.. Second event is executing.
