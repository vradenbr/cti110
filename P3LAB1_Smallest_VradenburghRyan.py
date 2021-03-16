num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2:
    var1 = num2
else:
    var1 = num1
    
if var1 > num3:
    var2 = num3
else:
    var2 = var1
       
print(var2)