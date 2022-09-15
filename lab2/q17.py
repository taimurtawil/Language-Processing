from math import sqrt
def minbound(x):
    i=0
    while i<100:
        x = sqrt(x)
        print(x)
        i+=1
    print(x)

minbound(float(input("Enter any Number: ")))