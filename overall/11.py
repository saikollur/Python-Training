import multiprocessing

def change_normal(num):
    print("\n[Child] Received normal number:", num)
    num = 50
    print("[Child] Changed normal number to:", num)

def change_shared_value(num):
    print("\n[Child] Shared Value before:", num.value)
    num.value = 50
    print("[Child] Shared Value after:", num.value)

def change_shared_array(arr):
    print("\n[Child] Array before change:", list(arr))
    for i in range(len(arr)):
        arr[i] = arr[i] * 2
    print("[Child] Array after change:", list(arr))

if __name__ == "__main__":

    print("=========== PART 1 : Processes DO NOT share memory ===========")
    number = 10
    p1 = multiprocessing.Process(target=change_normal, args=(number,))
    p1.start()
    p1.join()

    print("[Parent] Value after child process:", number)


    print("\n=========== PART 2 : Using multiprocessing.Value ===========")
    shared_number = multiprocessing.Value('i', 10)
    p2 = multiprocessing.Process(target=change_shared_value, args=(shared_number,))
    p2.start()
    p2.join()

    print("[Parent] Shared Value after child process:", shared_number.value)


    print("\n=========== PART 3 : Using multiprocessing.Array ===========")
    shared_array = multiprocessing.Array('i', [1, 2, 3, 4, 5])
    p3 = multiprocessing.Process(target=change_shared_array, args=(shared_array,))
    p3.start()
    p3.join()

    print("[Parent] Shared Array after child process:", list(shared_array))
