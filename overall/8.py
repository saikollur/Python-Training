import threading
import time

start_event = threading.Event()


def worker(id):
    print(f"Worker {id} is ready and waiting for signal...")
    start_event.wait()
    print(f"Worker {id} started working!")
    time.sleep(2)
    print(f"Worker {id} finished work.")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

print("Main thread preparing resources...")
time.sleep(5)

print("\nMain thread sending START signal!\n")

start_event.set()

for t in threads:
    t.join()

print("All workers completed.")
