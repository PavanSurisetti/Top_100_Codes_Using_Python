#string_palindrome_or_not
str=input("Enter a String:")
if(str==str[::-1]):
    print("String Palindrome")
else:
    print("Not a String Palindrome")