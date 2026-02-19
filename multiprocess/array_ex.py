import multiprocessing

def access(array):
    print("Acessing array elements: ",array[2])
    
if __name__ == "__main__":
    array = multiprocessing.Array('i', [1,2,3,4,5])
    p1 = multiprocessing.Process(target=access, args=(array,))
    p2 = multiprocessing.Process(target=access, args=(array,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
