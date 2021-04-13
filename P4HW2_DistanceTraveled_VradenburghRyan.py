# CTI-110
# P4HW2 - Distance Traveled
# 13 April 2021
# Ryan Vradenburgh
#

''' 
Define valid_number: Checks if changing the input to a float returns a ValueError.  
This allows the program to only accept valid input that won't crash the program.

Section 1: Starts a while loop for the user to change data later.
Accepts user input to define speed. The input is validated by valid_number() and,
if valid, assigned to the variable "speed" and converted to a float.

Section 2: Accepts user input to define duration of travel in hours.  
The input is validated by valid_number() and, if valid, is checked to verify it is not less than or equal to 0.
If the input passes these checks it is assigned to the variable "time".  
If the validation fails, the user is asked to input valid data.

Section 3: Creates a tabular view to display the data.
Calculates the range from 1 to the "time" variable and generates an entry for them distance traveled 
for each number in the range by multiplying "i" in range and "speed".  the range() function does not include the last entry in the range()
command so, rather than use time + 1, this program calculates the last entry seperately to allow for the differences
when the "time" variable is a float that does not end in .0.  The program calculates both the integer 
and float of "time" to give the user the most exact result.  The means that sometimes the last entry in the table is a float

Section 4: Asks for input if the user wants to change the "time" variable.  If the user does, they are
looped back to Section 2.  If they do not, the program ends.  The input data is validated to ensure only 
"yes" and "no" parameters are allowed.
'''

# Input validation to verify only numbers are entered. 
# Otherwise a non-float could crash the program.
def valid_number(x):
    try:
        return float(x)
    except ValueError:
        return False

def main():
# This program will calculate the distance traveled, given a speed and time traveled.


    # Section 1
    # Get user input of car's speed and validate that it is a float
    speed_input = False
    while speed_input == False:
        speed = input("\nEnter car's speed: ")
        if valid_number(speed):
            speed = float(speed) 
            speed_input = True
        else:
            print("\nError! That is not a valid speed!")

    # Section 2
    continue_tf = True
    while continue_tf == True:
        # Get user input for time traveled
        time_input = False
        time_error = "\nError! Time entered should be a number >0"
        while time_input == False:
            time = input("\nEnter time traveled: ")
            # Validate that the entry is a float and is a positive number greater than 0
            if valid_number(time):
                if float(time) <= 0:
                    print(time_error)
                # We are left with valid data and convert it to a float
                else:
                    time = float(time)
                    time_input = True
            else:
                print(time_error)

        # Section 3
        # Set tabular format header
        print("\n{:<8} {:<8}".format('Time', 'Distance')) 
        print("---------------------")

        # Calculate distance traveled from 1 to the time entered in Section 2
        for i in range(1, int(time)):
            print("{:<8} {:<8}".format(i, i * speed))
        
        # Checks if the time entered ends with a .0. If it does,
        # print the the last line. I did not use time + 1 in range() 
        # because I wanted to be able to display the time entered accurately.
        if str(time).endswith('.0'):
            print("{:<8} {:<8}".format(int(time), time * speed))
        else:
            # If time entered is a float, print it at the end of the table
            print("{:<8} {:<8}".format(int(time), int(time) * speed))
            print("{:<8} {:<8}".format(time, time * speed)) 
        
        # Section 4
        # Determine if the user wants to enter a different time
        validator = False
        while validator == False:
            new_input = input("\nWould you like to enter a different time? (y/n) ")
            # If the answer is "no" end the loops
            if new_input.lower() == "n" or new_input.lower() == "no":
                continue_tf = False
                validator = True
            # If input is "yes" end the validator loop and the continue_tf loop takes the user back
            # to Section 2 to enter a new time
            elif new_input.lower() == "y" or new_input.lower() == "yes":
                validator = True
            else:
                print("\nError! That is not a valid input!")
               
main()