##Write a program which calls the function getgrade() repeatedly until getgrade() 
# returns a valid grade. getgrade() should prompt for and read in from the keyboard 
# an integer in the range 0 to 100 and return it to the caller. If, however, 
# the grade entered is outside the range 0 to 100 inclusive, getgrade() should 
# raise a RuntimeError exception, indicating an invalid grade was entered. 
# When your program receives a valid grade from getgrade(), it should display 
# in which quartile the grade is in: first (75-100), second (50-74), third (25- 49), 
# or fourth (0-24).

def getgrade(x):
    if(x<= 100 and x>=0):
        if (x>= 75 and x<=100):
            print('First Quartile')
        elif(x<75 and x>= 50):
            print('Second Quartile')
        elif(x<50 and x >=25 ):
            print('Third Quartile')
        else:
            print('Fourth Quartile')
        
    
    else:
        raise RuntimeError("Not valid grade")
    

try:
    getgrade(int(input('Enter Grade: ')))
except RuntimeError as emsg:
    print(emsg)
    