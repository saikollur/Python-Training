import multiprocessing
import math

def heavy_calculation(n):
    result = 0
    for i in range(1, 10000):
        result += math.sqrt(n*i)
    print(f"Result for {n} computed:", result)

if __name__ == '__main__':

    inputs = [10, 20, 30, 40]
    processes = []

    for val in inputs:
        p = multiprocessing.Process(target=heavy_calculation, args=(val,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Scientific simulation done using multiprocessing.")

Result for 10 computed: 2108026.3368195645
Result for 20 computed: 2981199.4353699144
Result for 30 computed: 3651208.719064784
Result for 40 computed: 4216052.673639129
Scientific simulation done using multiprocessing.
