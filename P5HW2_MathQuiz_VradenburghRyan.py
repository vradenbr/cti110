# A simple program that generates 2 random numbers and adds or subtracts them based on user input
# 28APR2021
# CTI-110 P5HW2 - Math Quiz
# Ryan Vradenburgh
#
'''
BEGIN

Menu Function:
    Option 1: Add random numbers
    Option 2: Subtract random numnbers
    Option 3: Exit Program
    Accept User Input
    Return User Input

 Add_2_rand Function:
    Passed the add or subtract option selected from menu()
    Generate 2 random numbers between 1 and 1000
    Take user input as an integer 
    WHILE the user is playing
        IF user selected add: 
            add the two random numbers, assign the sum to variable "result", and ask the user to guess the sum
        ELSE IF user selected subtract
            subtract number 2 from number 1, assign the result to variable "result",  and ask user to guess the result
        incriment the guess counter
        IF the users answer equals the result:
            Say Congrats and list the number of responses
        ELSE IF the guess is higher than the result:
            Say too high and try again
        ELSE:
            Say guess is too low, try again

Main Function:
    WHILE playing the game:
        call menu function
        IF menu selection equals 1:
            call add_2_rand function and pass "1" as argument
        ELSE IF menu selection equals 2:
            call add_2_rand function and pass "1" as argument
        ELSE IF menu selection equals 3:
            Exit 
        ELSE:
            Input must be invalid, request user try again.

END
'''
import random

# Define menu function
def menu():
    choices = {}
    choices['1'] = "Add Random Numbers"
    choices['2'] = 'Subtract Random Numbers'
    choices['3'] = 'Exit'
    print('MAIN MENU\n-------------------\n')
    for option in choices:
        # Format menu how I want it to look
        print("{:<4}".format(''),option,')', choices[option])
    # Take user input 
    selection = input(': ')
    # Return user input to calling function
    return selection

# Define add_2_rand function
def add_2_rand(option):
    correct = False
    guesses = 0
    # Generate 2 random numbers
    rand_1 = random.randint(1,1000)
    rand_2 = random.randint(1,1000)
    while correct == False:
        # if argument passed from main() is 1, add the numbers
        if option == 1:
            print("{:<1}".format(''),rand_1,'\n+',rand_2)
            # Convert user input to integer 
            guess = int(input('Enter Answer: '))
            result = rand_1 + rand_2
        # if argument passed from main() is 2, subtract the numbers
        elif option == 2:
            print("{:<1}".format(''),rand_1,'\n-',rand_2)
            # Convert user input to integer 
            guess = int(input('Enter Answer: '))
            result = rand_1 - rand_2
        # Incriment guess counter
        guesses += 1
        # Congratulate if guess was correct
        if guess == result:
            print('\nCorrect!\nNumber of guesses: ',guesses,'\n')
            correct = True
        # Try again if guess was too high
        elif guess > result: 
            print('\nToo High, Try again\n')
        # Anything else must be too low, try again
        else:
            print('\nToo Low, Try Again\n')
# Define main function
def main():
    playing = True
    while playing == True:
        # Call menu function
        selection = menu()
        # If user selects option 1 call add_2_rand function and pass argument 1
        if selection == "1":
            add_2_rand(1)
        # If user selects option 2 call add_2_rand function and pass argument 2
        elif selection == '2':
            add_2_rand(2)
        # If user selects option 3, exit
        elif selection == "3":
            print('\nThanks for playing!')
            playing = False
        # Anything else is invalid
        else:
            print('\nThat is not a valid option, Try again\n')
main()