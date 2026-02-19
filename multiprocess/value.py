import multiprocessing

def access(value):
    value.value += 1
    
if __name__ == "__main__":
    value = multiprocessing.Value('i', 0)
    p1 = multiprocessing.Process(target=access, args=(value,))
    p2 = multiprocessing.Process(target=access, args=(value,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Final Value:", value.value)
