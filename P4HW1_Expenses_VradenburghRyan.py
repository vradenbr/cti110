# CTI-110
# P4HW1 - Expenses
# Ryan Vradenburgh
# 30 March 2021

''' 
Section 1: Contains 2 inputs, the first input asks for the starting account balance, the second input asks for the first expense.  
(It is presumed that there will be a minimum of one expense).  These inputs are assigned to variables and a third variable is created to store the 
value of the account after the expense has been deducted.

Section 2: Assigns the "add_input" boolean a value of "True" to assist with the "While" loop.  
Assigns the expense "counter" variable a value of "1" since there has already been one expense entered.
Begins the While loop.

Section 3: Asks the user if they want to enter additional expenses.  An input validation is done to determine their response.
If the response is a yes, go to Setion 4
If the response is a no, go to Section 5
If the response is neither yes or no, the input is determined to be invalid and is rejected, looping the user back to the top of Section 3.

Section 4: Requests the amount of the expense.  If the amount of the expense is greater than the available balance in the account, the 
entry is rejected and the user is looped back to Section 3.  
If the expense is valid the "acct_bal" variable is updated to the new amount and the counter is incremented to display that a new expense 
has been entered.  
The program will loop back to Section 3.

Section 5: If the user does not want to enter anotherr expense they are presented with the starting balance of the account, the total
number of expenses entered, and the current balance of the account. The "add_input" boolean is set to "False" to end the loop, and the program exits.

'''

def main():

    # Section 1
    # Get starting balance
    start_bal = float(input("What is the current balance of your Account? $"))
    # Get first expense amount
    expense = float(input("\nWhat is the amount of expense 1? $"))
    # Subtract expense from starting balance
    acct_bal = start_bal - expense
    
    # Section 2
    add_input = True
    counter = 1
    while add_input == True:
        # Section 3
        # Ask if the user would like to enter another expense.
        new_baL = input("\nWould you like to enter another expense? (y/n) ")
        if new_baL.lower() == "y" or  new_baL.lower() == "yes":
            # Section 4
            # Get the amount of the expense.
            expense = float(input("\nWhat is the amount of expense " + str(counter+1) + "? $"))
            if expense > acct_bal:
                # Inform the user they do not have enough funds in the account and that the expense will not be accepted.
                print("\nYou have insufficient funds for this expense! Your balance is only ${:.2f}".format(acct_bal), "\nThis transaction will not be added. ")
                continue
            # Subtract the expense from the account balance
            acct_bal -= expense
            # Incriment the counter to track the number of expenses
            counter += 1


        elif new_baL.lower() == "n" or  new_baL.lower() == "no":
            # Section 5
            # Print visual deliminator
            print('\n******************************************************')
            # Print starting balance
            print("\nYour starting balance was ${:.2f}".format(start_bal))
            # Print the number of expenses entered
            print("\nYou entered", counter, "expenses")
            # Print the current balance of the account
            print("\nYour current balance is: ${:.2f}".format(acct_bal))
            # Print visual deliminator
            print('\n******************************************************')
            add_input = False
        else:
            # Inform the user that they have entered invalid information
            print("\nYou have not provided a valid input, Please try again")

main()