import sys   # needed to access command line arg

#global variables
tokenindex = -1
token = ''

def main():
   try:
      parser()         # call the parser
   except RuntimeError as emsg:
      print(emsg)

def advance():
   global tokenindex, token
   tokenindex += 1     # move tokenindex to next token
   # check for null string or end of string
   if len(sys.argv) < 2 or tokenindex >= len(sys.argv[1]):
      token = ''      # signal the end by returning null string
   else:
      token = sys.argv[1][tokenindex]

def consume(expected):
   if expected == token:
      advance()
   else:
      raise RuntimeError('Expecting ' + expected)

def parser():
   advance()   # prime token with first character
   S()         # call function for start symbol
   # test if end of input string
   if token != '': 
      print('Garbage following <S>-string')
      
def S():
    while token == 'a':
        advance()
    B()
def B():
    while token == 'b':
        advance()
    C()
def C():
    consume('c')
    if(token == 'd'):
        advance()
    elif(token == 'e'):
        advance()
        
    consume('f')
main()

## (base) taimurtawil@client172-51 lab4 % python q3.py cf 

# (base) taimurtawil@client172-51 lab4 % python q3.py cdf
 
# (base) taimurtawil@client172-51 lab4 % python q3.py cef

# (base) taimurtawil@client172-51 lab4 % python q3.py aabbcf

# (base) taimurtawil@client172-51 lab4 % python q3.py acf   

# (base) taimurtawil@client172-51 lab4 % python q3.py bcf

# (base) taimurtawil@client172-51 lab4 % python q3.py    
# Expecting c

# (base) taimurtawil@client172-51 lab4 % python q3.py cdef
# Expecting f

# (base) taimurtawil@client172-51 lab4 % python q3.py cff 
# Garbage following <S>-string

# (base) taimurtawil@client172-51 lab4 % python q3.py abc
# Expecting f