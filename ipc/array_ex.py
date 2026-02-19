import multiprocessing

def oneUp(arr):
    for i in range(len(arr)):
        print(arr[i] + 1)
def twoUp(arr):
    for i in range(len(arr)):
        val = arr
        print(arr[i] + 2)

if __name__ == "__main__":
    arr = multiprocessing.Array('i', [1, 2, 3])

    p1 = multiprocessing.Process(target=oneUp, args=(arr,))
    p2 = multiprocessing.Process(target=twoUp, args=(arr,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

    print("Sharing array between processes.")
