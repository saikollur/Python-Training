import multiprocessing
import time

def primes(rand):
    count = 0
    for num in range(2, rand):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            count += 1
    return count

def single():
    start = time.time()
    primes(60000)
    primes(70000)
    primes(80000)
    end = time.time()
    print("Single process is time:", end - start)


def multi():
    start = time.time()

    p1 = multiprocessing.Process(target=primes, args=(1000,))
    p2 = multiprocessing.Process(target=primes, args=(2000,))
    p3 = multiprocessing.Process(target=primes, args=(3000,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    end = time.time()
    print("MUltiprocessing is taking time: ", end-start)

if __name__ == "__main__":
    single()
    multi()

----------------------------------------
Output:

Single process is time: 0.25139832496643066
MUltiprocessing is taking time:  0.13344335556030273
