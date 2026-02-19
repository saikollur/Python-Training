import multiprocessing

def accessValue(val):
    val.value += 1

if __name__ == "__main__":
    val = multiprocessing.Value('i', 10)

    p1 = multiprocessing.Process(target=accessValue, args=(val,))
    p2 = multiprocessing.Process(target=accessValue, args=(val,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(val.value)
    print("Both processes accessed the Value.")
