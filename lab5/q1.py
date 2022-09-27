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
    if token == 'a' or token == 'b' or token == 'c' or token == '':
        A()
        B()
        C()
        
def A():
    if token == 'a':
        advance()
    elif token == 'b' or token == 'c' or token == '':
        pass
    else:
        raise RuntimeError('Expecting a, b, c, or EOF marker')
    
def B():
    if token == 'b':
        advance()
    elif token == 'c' or token == '':
        pass
    else: 
        raise RuntimeError('Expecting b, c, or, EOF marker')
def C():
    if token == 'c':
        advance()
    elif token == '':
        pass
    else:
        raise RuntimeError('Expecting c or EOF marker') 
    
main()

# (base) taimurtawil@client172-51 Lab5 % python q1.py abc

# (base) taimurtawil@client172-51 Lab5 % python q1.py ac  

# (base) taimurtawil@client172-51 Lab5 % python q1.py bc

# (base) taimurtawil@client172-51 Lab5 % python q1.py a 

# (base) taimurtawil@client172-51 Lab5 % python q1.py b 

# (base) taimurtawil@client172-51 Lab5 % python q1.py c

# (base) taimurtawil@client172-51 Lab5 % python q1.py   

# (base) taimurtawil@client172-51 Lab5 % python q1.py aaa
# Expecting b, c, or, EOF marker

# (base) taimurtawil@client172-51 Lab5 % python q1.py abcd
# Garbage following <S>-string

# (base) taimurtawil@client172-51 Lab5 % python q1.py aba   
# Expecting c or EOF marker

# (base) taimurtawil@client172-51 Lab5 % python q1.py acb 
# Garbage following <S>-string