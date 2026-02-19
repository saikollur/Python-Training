import multiprocessing

def share(start, end, arr, result):
    total = 0
    for i in range(start, end):
        total += arr[i]
    result.value = total

if __name__ == "__main__":
    arr = multiprocessing.Array('i', [1, 2, 3, 4, 5, 6])

    res1 = multiprocessing.Value('i', 0)
    res2 = multiprocessing.Value('i', 0)

    mid = len(arr) // 2

    p1 = multiprocessing.Process(target=share, args=(0, mid, arr, res1))
    p2 = multiprocessing.Process(target=share, args=(mid, len(arr), arr, res2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"After dividing, first half value: {res1.value} and Second half value: {res2.value}")
