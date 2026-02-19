import multiprocessing

def process1(queue):
    print("I'm process 1")
    queue.put("Sending message to process 2 from me.")
def process2(queue):
    print(queue.get())

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=process1, args=(queue,))
    p2 = multiprocessing.Process(target=process2, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
