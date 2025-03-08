#Remove_the_vowels_from_a_String
str=input("Enter a String:").lower()
vowels=['a','e','i','o','u']
new_str=''
for i in str:
    if i not in vowels:
        new_str+=i
print(f'Before Removing The vowels :{str}\nAfter Removing The vowels :{new_str}')