import threading

lock = threading.Lock()

def worker(infile, outfile):
    try:
        with open(infile, "r") as f:
            data = f.read()

        result = f"{infile} -> {data.upper()}\n"

        with lock:
            with open(outfile, "a") as f:
                f.write(result)

        print(f"{infile} processed by {threading.current_thread().name}")

    except FileNotFoundError:
        print(infile, "not found")

open("a.txt","w").write("python is easy")
open("b.txt","w").write("threading needs lock")
open("c.txt","w").write("race condition avoided")

open("output.txt","w").close()

files = ["a.txt","b.txt","c.txt"]
threads = []

for f in files:
    t = threading.Thread(target=worker, args=(f,"output.txt"))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Done safely!")
