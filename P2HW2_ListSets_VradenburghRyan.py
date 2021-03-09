# CTI-110
# P2HW2 - List and Sets
# Ryan Vradenburgh 
# 8 March 2021
#

# Pseudocode Block
"""
The first operation asks the user to input ten numbers, which are appended to a list called input_list, which is printed to the terminal.

The second operation determines the lowest number in the list and prints it to the terminal.

The third operation determines the highest number in the list and prints it to the terminal.

The fourth operation generates the sum of all the numbers in the list and prints it to the terminal.

The fith operation averages the numbers in the list and prints the average to the terminal.

The sixth operation converts the list to a set.

The seventh and final operation prints the set to the terminal.
"""

# Request user input for ten numbers and create a list 
input_list = list()
input_list.append(int(input('Please enter a number (1 of 10): ')))
input_list.append(int(input('Please enter a number (2 of 10): ')))
input_list.append(int(input('Please enter a number (3 of 10): ')))
input_list.append(int(input('Please enter a number (4 of 10): ')))
input_list.append(int(input('Please enter a number (5 of 10): ')))
input_list.append(int(input('Please enter a number (6 of 10): ')))
input_list.append(int(input('Please enter a number (7 of 10): ')))
input_list.append(int(input('Please enter a number (8 of 10): ')))
input_list.append(int(input('Please enter a number (9 of 10): ')))
input_list.append(int(input('Please enter a number (10 of 10): ')))
print('Here is your list: ', input_list)

# Determine the lowest number in the list
min_list = min(input_list)
print('The lowest number is: ', min_list)

# Determine the highest number in the list
max_list = max(input_list)
print('The highest number is: ', max_list)

# Generate the sum of all numbers in the list
sum_list = sum(input_list)
print('The sum of all the numbers is: ', sum_list)

# Determine the average of the numbers in the list
avg_list = sum_list/len(input_list)
print('The average of the numbers is: ', avg_list)

# Convert the input list to a set
input_set = set(input_list)
print('Displayed as a set: ', input_set)