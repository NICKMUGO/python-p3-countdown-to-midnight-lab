# your code goes here!
import time
def countdown(seconds):
    while seconds > 0:
        print(f"{seconds} SECOND(S)!")
        seconds -= 1
    print("HAPPY NEW YEAR!")
def countdown_with_sleep(seconds):
    while seconds > 0:
        print(f"{seconds} SECOND(S)!")
        time.sleep(1)
        seconds -= 1
    print("HAPPY NEW YEAR!")
countdown(10)
countdown_with_sleep(10) 
