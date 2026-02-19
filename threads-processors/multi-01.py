import multiprocessing

def introduce(name, id):
    print(f"He is {name} and his id is {id}")
    print("Welcome to the team")
if __name__ == '__main__':

    p1 = multiprocessing.Process(target = introduce, args = ("Sai", "1"))
    p2 = multiprocessing.Process(target = introduce, args = ("Krishna", "2"))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


----------------------------------------
Output:

He is Sai and his id is 1
Welcome to the team
He is Krishna and his id is 2
Welcome to the team
