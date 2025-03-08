#check_alphabet_or_not
import string
alphabets=list(string.ascii_letters)
char=input("Enter a character:")
if char in alphabets:
    print(f'{char} is an Alphabet')
else:
    print(f'{char} is Not an Alphabet')