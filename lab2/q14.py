
# 1/1! + 1/2! + .. + 1/n!
 
# Function to find factorial of a number
def factorial(n):
    res = 1
    for i in range(2, n + 1):
            res *= i
    return res
         
# A Simple Function to return value
# of 1/1! + 1/2! + .. + 1/n!
def sum(n):
    s = 0.0
     
    for i in range(1, n + 1):
        s += 1.0 / factorial(i)
    print(s + 1)# so that it starts with 2 instead of 1
 
# Driver program to test above functions
n = 100
sum(n)
#this sum is = to e
