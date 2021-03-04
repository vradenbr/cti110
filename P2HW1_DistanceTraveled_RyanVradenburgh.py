# This program will calculate the distance traveled, given a speed and time traveled.
# 3 March 2021
# Ryan Vradenburgh
#

# Get user input of car's speed
speed = float(input("Enter car's speed: "))


# Get user input for time traveled
time = float(input("Enter time traveled in hours: "))

# get some space
print()

# Print the entered values
print("Speed entered:", speed, "MPH.")
print("Time entered: ", time, "hours.")

# Get some space
print()

# Calculate distance
print("Distance traveled:", speed * time, "miles.")
