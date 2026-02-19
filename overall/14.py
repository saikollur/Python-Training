import time
import threading
import multiprocessing

def cpu_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

def single_process(n):
    start = time.time()
    cpu_task(n)
    cpu_task(n)
    cpu_task(n)
    cpu_task(n)
    end = time.time()

    print("Single Process Time:", round(end - start, 3), "seconds")

def multi_threading(n):
    start = time.time()
    threads = []
    for _ in range(4):
        t = threading.Thread(target=cpu_task, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print("Multithreading Time:", round(end - start, 3), "seconds")

def multi_processing(n):
    start = time.time()
    processes = []
    for _ in range(4):
        p = multiprocessing.Process(target=cpu_task, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

    end = time.time()
    print("Multiprocessing Time:", round(end - start, 3), "seconds")

if __name__ == "__main__":
    N = 20_000_000
    single_process(N)
    multi_threading(N)
    multi_processing(N)
