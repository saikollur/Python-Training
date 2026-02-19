import multiprocessing
import time

def train(dataChunk):
    print(f"Training model on data chunk {dataChunk}")
    time.sleep(2)
    print(f"Finished training on data chunk {dataChunk}")

if __name__ == '__main__':
    
    dataChunks = [1, 2, 3, 4]
    processes = []

    for chunk in dataChunks:
        p = multiprocessing.Process(target=train, args=(chunk,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All models trained using multiprocessing.")

Training model on data chunk 1
Training model on data chunk 2
Training model on data chunk 3
Training model on data chunk 4
Finished training on data chunk 1
Finished training on data chunk 2
Finished training on data chunk 3
Finished training on data chunk 4
All models trained using multiprocessing.
