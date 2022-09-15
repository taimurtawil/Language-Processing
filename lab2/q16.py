def noddnumbers( n):
    while(n<0):
        n=int(input("The number you submitted was negative! Try again: "))
    sum = 1
    count = 0
    temp = 1
    while(count<n-1):
        temp += 2
        sum += temp
        count += 1
    return sum
print(noddnumbers(int(input("Enter a Positive Number: "))))
## the sum of the first n positive integers is just n squared