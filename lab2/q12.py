# # 12. Write a program that reads in a text file that consists of some standard English text. 
# # Your program should count the number of occurrences of each letter of the alphabet, 
# # and display each letter with its count, in the order of increasing count. 
# # What are the six most frequently used letters?

infile = open('lab2.txt', 'r')
source = infile.read()
d={}
for char in set(source):
    if char.isalpha():
        d[char]=source.count(char)
sorted_d = sorted(d.items(), key = lambda kv: kv[1])
print('\nLetter count' + str(sorted_d))

x = 6
most_freq = sorted_d[-x:]
print('\nthe most frequent letters are: ' + str(most_freq))