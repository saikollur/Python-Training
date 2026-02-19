import threading
import time

event = threading.Event()

def cheifGuest():
    time.sleep(2)
    print("Guest has arrived. Start the activities.")
    event.set()

def dancers():
    print("Dancers waiting for the chief guest to arrive.")
    event.wait()
    print("Starting the dance.")

def openingCeremony():
    print("Opening ceremony speech is delayed.")
    event.wait()
    print("Opening speech is happening.")

t1 = threading.Thread(target=openingCeremony)
t2 = threading.Thread(target=dancers)
t3 = threading.Thread(target=cheifGuest)

t1.start()
t2.start()
t3.start()

----------------------------------------
Output:

Opening ceremony speech is delayed.
Dancers waiting for the chief guest to arrive.
Guest has arrived. Start the activities.
Starting the dance.
Opening speech is happening.
