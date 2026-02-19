import multiprocessing

def filterApply(filter, image_no):
    print(f"Applied {filter} to image {image_no}")

if __name__ == '__main__':
    processes = []

    for i in range(1, 5):
        p = multiprocessing.Process(target=filterApply, args=("vintage", i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Applied same filter to multiple images using multi-processing")

Applied vintage to image 1
Applied vintage to image 2
Applied vintage to image 3
Applied vintage to image 4
Applied same filter to multiple images using multi-processin
