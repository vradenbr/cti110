# Define your function here 
def miles_to_laps(user_miles):
    laps = float(user_miles) / 0.25
    return laps

if __name__ == '__main__':
    # Type your code here. Your code must call the function. 
    laps = miles_to_laps(input())
    print ('{:.2f}'.format(laps))