import sys   # needed to access command line arg

#global variables
tokenindex = -1
curchar = ''

def main():
   parser()      # call the parser

def parser():
   advance()   # prime curchar with first character
   if S():
      if curchar == '': 
         print('String in language')
      else:
         print('Garbage following string')
   else:
      print('String not in language')

def S():
   return A() and C()

def A():
   return consume('a') and consume('b')

def C():
   global tokenindex
   save = tokenindex
   if C1():
      return True
   else:                  # backtrack if C1() doesn't work
      tokenindex = save
      return C2()
def C1():
   return consume('c') and C()
def C2():
   return consume('d')

def advance():
   global tokenindex, curchar
   tokenindex += 1    # move tokenindex to next token
   # check for null string or end of string
   if len(sys.argv) < 2 or tokenindex >= len(sys.argv[1]):
      curchar = ''    # signal the end by returning ''
   else:
      curchar = sys.argv[1][tokenindex]

def consume(expected):
   if expected == curchar:
      advance()
      return True
   else:
      return False
      
def S():
    return A() and B() and C()
        
def A():
    global tokenindex
    temptokenindex = tokenindex
    if A1():
        return True
    else:
        tokenindex = temptokenindex
        return A2()
def A1():
    return consume('a')
def A2():
    return True
def B():
    global tokenindex
    temptokenindex = tokenindex
    if B1():
        return True
    else:
        tokenindex = temptokenindex
        return B2()
def B1():
    return consume('b')
def B2():
    return True
def C():
    global tokenindex
    temptokenindex = tokenindex
    if C1():
        return True
    else:
        tokenindex = temptokenindex
        return C2()
    
def C1():
    return consume('c')
def C2():
    return True
    
main()

# (base) taimurtawil@client169-234 Language-Processing % python q9.py abc
# String in language

# (base) taimurtawil@client169-234 Language-Processing % python q9.py ac 
# String in language

# (base) taimurtawil@client169-234 Language-Processing % python q9.py bc
# String in language

# (base) taimurtawil@client169-234 Language-Processing % python q9.py a   
# String in language

# (base) taimurtawil@client169-234 Language-Processing % python q9.py b
# String in language

# (base) taimurtawil@client169-234 Language-Processing % python q9.py c 
# String in language

# (base) taimurtawil@client169-234 Language-Processing % python q9.py   
# String in language

# (base) taimurtawil@client169-234 Language-Processing % python q9.py aaa
# Garbage following string

# (base) taimurtawil@client169-234 Language-Processing % python q9.py abcd
# Garbage following string

# (base) taimurtawil@client169-234 Language-Processing % python q9.py aba 
# Garbage following string

# (base) taimurtawil@client169-234 Language-Processing % python q9.py acb
# Garbage following string
