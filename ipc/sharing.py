import multiprocessing

def share(s, e, q):
    total = 0
    for i in range(s, e + 1):
        total += i
    q.put(total)

if __name__ == "__main__":
    N = 10
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=share, args=(1, N//2, q))
    p2 = multiprocessing.Process(target=share, args=(N//2 + 1, N, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    result = q.get() + q.get()
    print("Final Sum:", result)
