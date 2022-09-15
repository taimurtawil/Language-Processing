def isPalindrome(s):
    return s == s[::-1]

if(isPalindrome(input("Enter a String: "))):
    print("The string you inputted is a palindrome!")
else:
    print("The string you inputted was not a palindrome. ): ")