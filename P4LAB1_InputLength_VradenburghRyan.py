user_text = input()

input_counter = 0
banned_chars = ['!', ',', ' ', '.']

for letter in user_text:
    if letter in banned_chars:
        continue
    else:
        input_counter += 1    
print(input_counter)
    
