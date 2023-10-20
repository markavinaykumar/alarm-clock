import time
import os

def set_alarm():
    try:
        hours = int(input("Enter the hour (0-23): "))
        minutes = int(input("Enter the minutes (0-59): "))
        alarm_time = (hours, minutes)
        return alarm_time
    except ValueError:
        print("Please enter a valid time.")
        return set_alarm()

def main():
    print("Welcome to the Alarm Clock App")
    alarm_time = set_alarm()
    while True:
        current_time = time.localtime()
        if (current_time.tm_hour, current_time.tm_min) == alarm_time:
            print("Time to wake up!")
            # You can add code to play a sound or show a notification here.
            break
        time.sleep(60)  # Check the time every 60 seconds

if __name__ == "__main__":
    main()
