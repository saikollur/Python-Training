# An online examination system must run a timer 
# while the student is answering questions. 
# Write a multithreading program to simulate this.

import threading
import time

event = threading.Event()
answer = None

def timer():
    time.sleep(5)
    event.set()
def getAnswer():
    global answer
    answer = input()
    event.set()

def questions():
    ques = ["Who is Indias current T20I captain?",
        "When did India win first T20 World Cup?",
        "Who scored fastest T20I century for India?",
        "Which Indian bowler has most T20I wickets?",
        "Against which team India played first T20I?"
    ]

    print("You have 5 seconds time to answer each question.")
    for q in ques:
        global answer
        answer = None
        print(q)
        event.clear()
        
        t1 = threading.Thread(target=timer)
        t2 = threading.Thread(target=getAnswer)

        t1.start()
        t2.start()

        event.wait()

        if answer is None:
            print("Time out.. Moving to next question.")
        else:
            print("Answer Submitted")

        t1.join()
        t2.join()

t = threading.Thread(target=questions)
t.start()
t.join()

print("Submit the test.")

Time out.. Moving to next question.
Against which team India played first T20I?
Time out.. Moving to next question.
Submit the test.


You have 5 seconds time to answer each question.

Who is Indias current T20I captain?
surya
Answer Submitted

When did India win first T20 World Cup?
2007
Answer Submitted

Who scored fastest T20I century for India?
rohit
Answer Submitted

Which Indian bowler has most T20I wickets?
Time out.. Moving to next question.

Against which team India played first T20I?
Time out.. Moving to next question.

Submit the test.
