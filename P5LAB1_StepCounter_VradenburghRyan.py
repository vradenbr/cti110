# Define your function here 
def steps_to_miles(user_steps):
    miles = int(user_steps) / 2000
    return miles    
if __name__ == '__main__':
    # Type your code here.
    miles = steps_to_miles(input())
    print ('{:.2f}'.format(miles))
    
    