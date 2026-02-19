# A background task must auto-save data 
# while a user continues working. Simulate this using threads.

import threading
import time

event = threading.Event()

def userWork():
    print("User is working on the blog.")
    time.sleep(2)

    print("User uploaded image.")
    event.set()
    time.sleep(2)

    print('User done with the article')
    event.set()
    time.sleep(2)

    print("User exiting the system.")
def autoSave():
    event.wait()
    print("Image data auto saved.")
    time.sleep(2)
    print("Article data auto saved saved.")
    event.clear()


t1 = threading.Thread(target=userWork)
t2 = threading.Thread(target=autoSave)

t1.start()
t2.start()

t1.join()

print("Work auto saved successfully!")


User is working on the blog.
User uploaded image.
Image data auto saved.
User done with the article
Article data auto saved saved.
User exiting the system.
Work auto saved successfully!
