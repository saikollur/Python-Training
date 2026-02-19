import threading
import time

temp = 28
humid = 80
def temperature():
    global temp
    for i in range(5):
        newTemp = temp
        newTemp += 1
        temp = newTemp
        print("Temperature (C) right now:", temp)
        time.sleep(1)
def humidity():
    global humid
    for i in range(5):
        newHumid = humid
        newHumid += 1
        humid = newHumid
        print("Humidity (%) right now:", humid)
        time.sleep(2)

t1 = threading.Thread(target=temperature)
t2 = threading.Thread(target=humidity)

t1.start()
t2.start()

t1.join()
t2.join()

print("Temperature and Humidity is being monitored.")


Temperature (C) right now: 29
Humidity (%) right now: 81
Temperature (C) right now: 30
Humidity (%) right now: 82
Temperature (C) right now: 31
Temperature (C) right now: 32
Humidity (%) right now: 83
Temperature (C) right now: 33
Humidity (%) right now: 84
Humidity (%) right now: 85
Temperature and Humidity is being monitored.
