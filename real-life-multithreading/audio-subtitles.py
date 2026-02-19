#A media player must play audio and display subtitles simultaneously. 
# Write a multithreading program to simulate this.


import threading
import time

def audio():
    for i in range(4):
        print("Playing audio.. ")
        time.sleep(2)

def subtitles():
    subtitles = [
    "Hello everyone", 
    "Your show is about to start.", 
    "Keep your mobile phones away.", 
    "Enjoy the show!"
    ]
    for sub in subtitles:
        print("Subtitles:",sub)
        time.sleep(2)
    
audio = threading.Thread(target=audio)
subtitle = threading.Thread(target=subtitles)

audio.start()
subtitle.start()

audio.join()
subtitle.join()

Playing audio.. 
Subtitles: Hello everyone
Playing audio.. 
Subtitles: Your show is about to start.
Playing audio.. 
Subtitles: Keep your mobile phones away.
Playing audio.. 
Subtitles: Enjoy the show!
