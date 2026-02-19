import multiprocessing

def increment(counter):
    for _ in range(1000):
        counter.value += 1

if __name__ == "__main__":
    counter = multiprocessing.Value('i', 0)
    processes = []

    for _ in range(5):
        p = multiprocessing.Process(target=increment, args=(counter,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Final counter value:", counter.value)
