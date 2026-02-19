# A chat application needs to send messages and receive messages 
# at the same time. Write a program using threads to simulate this behavior.


import threading
import time

event = threading.Event()
stop = False

def sender():
    global stop
    while True:
        msg = input("You: ").strip()

        if msg.lower() == "exit":
            stop = True
            event.set()
            print("You left the chat.")
            break

        event.set()

def receiver():
    replies = [
        "Hello",
        "I'm doing great!",
        "Okay, let's meet at 10 AM",
        "Bye"
    ]
    i = 0
    while not stop:
        event.wait()
        event.clear()

        if stop:
            break

        print("Friend:", replies[i % len(replies)])
        i += 1

t1 = threading.Thread(target=sender)
t2 = threading.Thread(target=receiver)

t1.start()
t2.start()

t1.join()


You: Hey
Friend: Hello
You: How are you doing?
Friend: I'm doing great!
You: Are you free tomorrow? I want to meet you!
Friend: Okay, let's meet at 10 AM
You: okay
Friend: Bye
You: exit
You left the chat.
