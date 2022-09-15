x = int(input("Enter a Positive Integer: "))
while (x < 0):
    x=int(input("The Number you submitted was not positive. Try again: "))

sum1 = 0
for i in range(1,x):
    if(x % i == 0):
        sum1 += i 
    
if(sum1 == x):
    print("The number is a perfect number!")
else:
    print("The number is not a perfect number ):")