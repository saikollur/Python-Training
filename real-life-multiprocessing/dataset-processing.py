import multiprocessing

def datasets():
    print(f"Dataset is being processed by {multiprocessing.current_process().name}")

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=datasets)
        p.start()
        p.join()

Dataset is being processed by Process-1
Dataset is being processed by Process-2
Dataset is being processed by Process-3
Dataset is being processed by Process-4
Dataset is being processed by Process-5
