import multiprocessing
import time

def parkingSlot(car, duration):
    print(f"{car} has reserved the spot for {duration} hours.")
    time.sleep(duration)
    print(f"{car} is checking out.")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=parkingSlot, args=("Car A", 3))
    p2 = multiprocessing.Process(target=parkingSlot, args=("Car B", 2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

----------------------------------------
Output:

Car A has reserved the spot for 3 hours.
Car B has reserved the spot for 2 hours.
Car B is checking out.
Car A is checking out.
