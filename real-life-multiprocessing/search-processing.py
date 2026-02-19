import multiprocessing

def search(doc, keyword):
    print(f"Searching '{keyword}' in part {doc}")

if __name__ == '__main__':

    docs = [1,2,3,4]
    keyword = "python"

    processes = []

    for part in docs:
        p = multiprocessing.Process( target=search, args=(part, keyword))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Keyword search completed using multiprocessing.")

Searching 'python' in part 1
Searching 'python' in part 2
Searching 'python' in part 3
Searching 'python' in part 4
Keyword search completed using multiprocessing.
