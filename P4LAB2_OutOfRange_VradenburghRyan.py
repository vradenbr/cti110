input_one = int(input())
input_two = int(input())

output_list = []

if input_one > input_two:
    print("Second integer can't be less than the first.")
else:
    while input_one <= input_two:
        output_list.append(input_one)
        input_one += 5
    
    for i in output_list:
        print(i,  end=' ')
    print()
    