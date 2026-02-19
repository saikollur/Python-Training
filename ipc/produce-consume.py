import multiprocessing

def makeNumbers(queue):
    print("Producing numbers..")
    for i in range(1,20):
        queue.put(i*2)
    queue.put(None)
def consumeNumbers(queue):
    while True:
        num = queue.get()
        if num is None:
            break
        print("Consumed:", num)

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=makeNumbers, args=(queue,))
    p2 = multiprocessing.Process(target=consumeNumbers, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Consumed all the numbers.")
