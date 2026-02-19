import multiprocessing

def oneUp(arr):
    for i in range(len(arr)):
        print(arr[i] + 1)
def twoUp(arr):
    for i in range(len(arr)):
        val = arr
        print(arr[i] + 2)

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    lis = manager.list([1, 2, 3])

    p1 = multiprocessing.Process(target=oneUp, args=(lis,))
    p2 = multiprocessing.Process(target=twoUp, args=(lis,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

    print("Sharing list between processes using Manager.")
