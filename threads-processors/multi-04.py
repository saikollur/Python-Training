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
    print(f"Primes below {rand}: {count}")

if __name__ == "__main__":

    p1 = multiprocessing.Process(target=primes, args=(1000,))
    p2 = multiprocessing.Process(target=primes, args=(2000,))
    p3 = multiprocessing.Process(target=primes, args=(3000,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

----------------------------------------
Output:

Primes below 1000: 168
Primes below 2000: 303
Primes below 3000: 430
