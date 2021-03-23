# CTI-110
# P3HW2 - Distance Traveled
# 22 March 2021
# Ryan Vradenburgh
#

''' 
Section 1: Accepts user input to define speed.  

Section 2: Accepts user input to define duration of travel in hours.  
If the number entered is "0" or a negative number, the input validation displays an error and sets the 
time traveled to one hour.

Section 3: Prints the speed, time traveled, and distance (time * speed)
'''

def main():
# This program will calculate the distance traveled, given a speed and time traveled.

    # Section 1
    # Get user input of car's speed
    speed = float(input("Enter car's speed: "))

    # Section 2
    # Get user input for time traveled
    time = float(input("\nEnter time traveled in hours: "))
    if time < 1:
        print("\n***********************************************************\n* Error ! time enterd should be >0 Time will be set to 1. *\n*********************************************************** ", )
        time = 1

    # Section 3
    # Print the entered values
    print("\nSpeed entered:", speed, "MPH.")
    print("\nTime entered: ", time, "hours.")

    # Calculate distance
    print("\nDistance traveled:", speed * time, "miles.")

main()