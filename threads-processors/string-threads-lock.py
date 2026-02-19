# Controlling shared access using LOCK

import threading

string = "It's Ind vs NZ match"
lock = threading.Lock()

def studentName(details):
    global string
    with lock:
        string += details
        print(string)

print("Intial String -", string)
t1 = threading.Thread(target = studentName, args = (" tomorrow at 7pm",))
t2 = threading.Thread(target = studentName, args = (". You can live stream on hotstar.",))

t1.start()
t2.start()

t1.join()
t2.join()

----------------------------------------
Output: 

Intial String - Its Ind vs NZ match
Its Ind vs NZ match tomorrow at 7pm
Its Ind vs NZ match tomorrow at 7pm. You can live stream on hotstar.
