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
    if token  == 'a':
        advance()
        B()
        consume('d')
    else:
        raise RuntimeError('Expecting an a')
def B():
    if(token == 'b' ):
        while(token == 'b'):
            advance()
            if(token == 'b'):
                advance()
            else:
                raise RuntimeError('expecting b')
    if(token == 'c'):
        advance()
    

main()

## (base) taimurtawil@client172-51 lab4 % python q2.py ad

# (base) taimurtawil@client172-51 lab4 % python q2.py acd

# (base) taimurtawil@client172-51 lab4 % python q2.py abbcd 

# (base) taimurtawil@client172-51 lab4 % python q2.py abbd  

# (base) taimurtawil@client172-51 lab4 % python q2.py abbbbd

# (base) taimurtawil@client172-51 lab4 % python q2.py abbbbcd

# (base) taimurtawil@client172-51 lab4 % python q2.py  
# Expecting an a

# (base) taimurtawil@client172-51 lab4 % python q2.py abd
# expecting b

# (base) taimurtawil@client172-51 lab4 % python q2.py abcd
# expecting b

# (base) taimurtawil@client172-51 lab4 % python q2.py adc  
# Garbage following <S>-string

# (base) taimurtawil@client172-51 lab4 % python q2.py accd
# Expecting d       
        
