import multiprocessing
x = 0

def change():
    global x
    x += 1
    print("Child (no share): x =", x)

def shared(x):
    x.value += 1
    print("Child (shared): x =", x.value)

if __name__ == "__main__":

    print("---- No shared memory ----")

    p1 = multiprocessing.Process(target=change)
    p1.start()
    p1.join()
    print("Main (no share): x =", x)

    print("\n---- With IPC ----")

    x = multiprocessing.Value('i', 0)
    p2 = multiprocessing.Process(target=shared, args=(x,))
    p2.start()
    p2.join()
    print("Main (shared): x =", x.value)
