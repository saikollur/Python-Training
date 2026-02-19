import threading
import random
import time

condition = threading.Condition()
buffer = []
maxi = 5
stop = threading.Event()

def producer(id):
    global buffer
    while not stop.is_set():
        item = random.randint(1, 1000)

        with condition:
            while len(buffer) == maxi and not stop.is_set():
                print(f"Buffer full → Producer {id} waiting")
                condition.wait()

            if stop.is_set():
                break

            buffer.append(item)
            print(f"Producer {id} produced {item} | Buffer: {buffer}")
            condition.notify_all()

        time.sleep(1)

def consumer(id):
    global buffer
    while not stop.is_set():
        with condition:
            while len(buffer) == 0 and not stop.is_set():
                print(f"Buffer empty → Consumer {id} waiting")
                condition.wait()

            if buffer:
                item = buffer.pop(0)
                print(f"Consumer {id} consumed {item} | Buffer: {buffer}")

            condition.notify_all()

        time.sleep(1.5)

producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]
consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(2)]


for t in producers:
    t.start()

for t in consumers:
    t.start()


time.sleep(10)
stop.set()

with condition:
    condition.notify_all()

for t in producers + consumers:
    t.join()

print("Program finished safely")
