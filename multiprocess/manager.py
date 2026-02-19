import multiprocessing

def access(list):
    list.append(list[0]+1)
    
if __name__ == "__main__":
    manager = multiprocessing.Manager()
    list = manager.list([20,30,40])

    p1 = multiprocessing.Process(target=access, args=(list,))
    p1.start()
    p1.join()
    print(list)
