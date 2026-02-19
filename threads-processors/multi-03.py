import multiprocessing

def val(a):
    a = a + 10
    print("Inside process a =", a)

if __name__ == "__main__":
    a = 5
    print("Before process, a =", a)

    p = multiprocessing.Process(target=val, args=(a,))
    p.start()
    p.join()

    print("After process, a =", a)


----------------------------------------
Output:

Before process, a = 5
Inside process a = 15
After process, a = 5
