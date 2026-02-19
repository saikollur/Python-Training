import threading
string = "Ind vs NZ match"
lock = threading.Lock()

def details(newStr):
    global string
    with lock:
        string += newStr
        print(string)

t1 = threading.Thread(target = details, args=(". Tomorrow at 7pm.", ))
t2 = threading.Thread(target = details, args=(" Watch it on hotstar.", ))

t1.start()
t2.start()

t1.join()
t2.join()
