import multiprocessing

def frames(num):
    print(f"{multiprocessing.current_process().name} rendered frame {num}")

if __name__ == '__main__':
    processes = []
    for i in range(1,5):
        p = multiprocessing.Process(target=frames, args=(i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print("Video frames rendered by using multiprocessing.")


Process-1 rendered frame 1
Process-2 rendered frame 2
Process-3 rendered frame 3
Process-4 rendered frame 4
Video frames rendered by using multiprocessing.
