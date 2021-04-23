# A simple program that generates a random number and allows the user to guess the number.
# 23APR2021
# CTI-110 P5HW1 - Random Number
# Ryan Vradenburgh
#
'''
BEGIN

Menu Function:
    Option 1: Play Game
    Option 2: Exit Program
    Accept User Input
    Return User Input

Game Function:
    Generate random number between 1 and 100
    Take user input as an integer 
    WHILE the user has not guessed correctly:
        IF guess is correct: 
            incriment guess counter
            congratulations, display guess counter and return to main menu
            end while loop
        ELSE IF guess is too low: 
            incriment guess counter
            tell user to try again
        ELSE IF guess is not correct and not too low (i.e. too high): 
            incriment guess counter
            tell user to try again

Main Function:
    WHILE playing the game:
        call menu function
        IF menu selection equals 1:
            call game function
        ELSE IF menu selection equals 2:
            allow program to exit
        ELSE:
            Input must be invalid, request user try again.

END
'''
import random

# Define menu function
def menu():
    choices = {}
    choices['1'] = "Play Game"
    choices['2'] = 'Exit'
    print('MAIN MENU\n-------------------\n')
    for option in choices:
        # Format menu how I want it to look
        print("{:<4}".format(''),option,')', choices[option])
    # Take user input 
    selection = input(': ')
    # Return user input to calling function
    return selection

# Define game function
def game():
    # Generate a random number 
    rand_num = random.randint(1,100)
    guess_correct = False
    guesses = 0
    while guess_correct == False:
        # Take user's guess and convert to an integer
        guess = int(input('Enter a number between 1 and 100: '))
        # If the guess is correct, congratulate the user
        if guess == rand_num:
            print('\nCongratulations!! You\'re a winner!')
            # Set to True to end the loop
            guess_correct = True
            #  Incriment guess counter
            guesses += 1
            print('Total guesses: ',guesses,'\n')
        # If the guess is too low, try again
        elif guess < rand_num:
            print('Too low, try again')
            # Incriment the guess counter
            guesses += 1
        # if the guess is too high, try again
        else:
            print('Too high, try again')
            # Incriment guess counter
            guesses += 1
# Define main function
def main():
    playing = True
    while playing == True:
        # Call menu function
        selection = menu()
        # If user selects option 1 call game function
        if selection == "1":
                game()
        # If user selects option 2 allow program to exit
        elif selection == "2":
            playing = False
        # Anything else is invalid
        else:
            print('\nThat is not a valid option, Try again\n')
main()