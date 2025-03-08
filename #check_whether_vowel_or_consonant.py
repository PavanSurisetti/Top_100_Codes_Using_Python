#check_whether_vowel_or_consonant
str=input("Enter a Character:").lower()
vowel=['a','e','i','o','u']
if(str in vowel):
    print(f"{str} is Vowel")
else:
    print(f"{str} is Consonant")
