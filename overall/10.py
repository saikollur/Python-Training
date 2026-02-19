import multiprocessing
import time

def generateNums(q1):
    for i in range(1,6):
        print("Generated:", i)
        q1.put(i)
        time.sleep(1)
    
    q1.put(None)

def calculateSqrs(q1, q2):
    while True:
        num = q1.get()
        if num is None:
            q2.put(None)
            break
        sq = num * num
        q2.put(sq)

def display(q2):
    while True:
        val = q2.get()
        if val is None:
            break
        print("Square:", val)

if __name__ == "__main__":
    
    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=generateNums, args=(q1,))
    p2 = multiprocessing.Process(target=calculateSqrs, args=(q1,q2))
    p3 = multiprocessing.Process(target=display, args=(q2,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
