# Unsyncronised Access

import threading
import time

text = ""

def write_text_unsync(word):
    global text
    temp = text
    time.sleep(0.2)
    temp += word
    text = temp
    print(text)

for word in ["Hello ", "World ", "From ", "Threads"]:
    t = threading.Thread(target=write_text_unsync, args=(word,))
    t.start()

----------------------------------------
Output:

Hello 
From 
World
Threads
