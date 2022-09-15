##Write a program that creates a dictionary whose key/value pairs are 'a'/1, 'b'/2, ..., 'z'/26. 
# Then prompt for and read in a letter, and display its corresponding number value obtained from your dictionary.
from string import ascii_lowercase as alc
d={}
num = 1
for i in alc:
    d[i] = num
    num+=1

x = input('Enter a Letter: ')
print(d[x])