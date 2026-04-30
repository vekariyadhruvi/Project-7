from datetime import datetime
import time

# Display current date and time and format dates into custom formats
def current_datetime():
    return datetime.now()

def formatted_datetime():
    now=datetime.now()
    return now.strftime("%m-%d-%Y %H:%M:%S")

# Calculate the difference between two dates
def date_difference(d1, d2):
    date1 = datetime.strptime(d1, "%d-%m-%Y")
    date2 = datetime.strptime(d2, "%d-%m-%Y")
    return abs((date2 - date1).days)

# Simple Stopwatch
def stopwatch():
    input("Press Enter to start stopwatch...")
    start=time.time()
    input("Press Enter to stop...")
    end=time.time()
    return round(end-start, 2)

# Countdown timer
def countdown(seconds):
    while seconds>0:
        print(f"\rTime left: {seconds} sec", end="")
        time.sleep(1)
        seconds-=1
    print("\nTime's up!")