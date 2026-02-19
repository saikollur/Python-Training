#Synchronised Access

import threading
import time

text = ""
lock = threading.Lock()

def write_text_unsync(word):
    global text
    with lock:
        temp = text
        temp += word
        text = temp
        print(text)

for word in ["Hello ", "World ", "From ", "Threads"]:
    t = threading.Thread(target=write_text_unsync, args=(word,))
    t.start()

----------------------------------------
Output: 

Hello
World
From
Threadss
