import multiprocessing

def pipe1(pipe):
    pipe.send("Pipe1: Hey there!")
    print(pipe.recv())

def pipe2(pipe):
    pipe.send("Pipe2: Hello, got your message.")
    print(pipe.recv())

if __name__ == "__main__":
    person1, person2 = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=pipe1, args=(person1,))
    p2 = multiprocessing.Process(target=pipe2, args=(person2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
