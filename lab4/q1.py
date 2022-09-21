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
    if token == 'a':
        advance()
        S()
        consume('b')
    elif token == 'c':
        advance()
    else:
        raise RuntimeError('Expecting a or c')
     
main()

## (base) taimurtawil@client172-51 lab4 % python q1.py c  

# (base) taimurtawil@client172-51 lab4 % python q1.py acb

# (base) taimurtawil@client172-51 lab4 % python q1.py aacbb

# (base) taimurtawil@client172-51 lab4 % python q1.py      
# Expecting a or c

# (base) taimurtawil@client172-51 lab4 % python q1.py ca
# Garbage following <S>-string

# (base) taimurtawil@client172-51 lab4 % python q1.py ab
# Expecting a or c

# (base) taimurtawil@client172-51 lab4 % python q1.py acbb
# Garbage following <S>-string

# (base) taimurtawil@client172-51 lab4 % python q1.py aacb
# Expecting b

# (base) taimurtawil@client172-51 lab4 % python q1.py bca 
# Expecting a or c