import threading
import time

def person1():
    print("Hey, hi")
    time.sleep(2)
    print("How are you doing")
def person2():
    print("Hello, nice to meet you.")
    time.sleep(2)
    print("I'm good. What about you?")

t1 = threading.Thread(target=person1)
t2 = threading.Thread(target=person2)

t1.start()
t2.start()

t1.join()
t2.join()
