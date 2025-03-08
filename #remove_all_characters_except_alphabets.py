#remove_all_characters_except_alphabets
import string
str=input("Enter a String:")
new_str=''
alphabets=list(string.ascii_letters)
for i in str:
    if i  in alphabets:
        new_str+=i
print(f'Before Removing The Alphabets:{str}\nAfter Removing The Alphabets:{new_str}')