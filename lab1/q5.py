list = []
i=0
while i < 10:
    x = int(input('Enter an Integer: '))
    list.append(x)
    i+=1
print("*******************")
j=0
while j < 10:
    print(list[j])
    j+=1
    
print("*******************")
t= 1 
while t <= 10:
    print(list[t*-1])
    t+= 1
print("*******************")    
a=1 
while a<=10:
    print(list.pop())
    a+=1
    

