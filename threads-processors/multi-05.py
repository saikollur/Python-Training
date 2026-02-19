import multiprocessing
import time

def producer(queue):
    for i in range(5):
        print(f"Producer putting: {i+1}")
        queue.put(i+1)
        time.sleep(1)

def consumer(queue):
    for i in range(5):
        data = queue.get()
        print(f"Consumer got: {data}")

if __name__ == "__main__":
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

----------------------------------------
Output:

Producer putting: 1
Consumer got: 1
Producer putting: 2
Consumer got: 2
Producer putting: 3
Consumer got: 3
Producer putting: 4
Consumer got: 4
Producer putting: 5
Consumer got: 5
