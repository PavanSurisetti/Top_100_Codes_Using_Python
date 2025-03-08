#no_of_vowels_in_a_string
str=input('Enter a String:').lower()
vowels=['a','e','i','o','u']
count=0
for i in str:
    if(i in vowels):
        count+=1
print(f'The vowel count in {str} is {count}')