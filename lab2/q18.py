def prinx(x):
    i = 0 
    while(i<=x):
        j=1
        while(j<=i):
            print(str(j) + " ", end=" ")
            j+=1
        print("")
        i+=1
        
prinx(int(input("Enter a Number: ")))