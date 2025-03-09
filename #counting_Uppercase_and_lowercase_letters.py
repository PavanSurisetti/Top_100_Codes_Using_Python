#counting_Uppercase_and_lowercase_letters
str=input('Enter a String:')
upp_count=0
low_count=0
for i in str:
    if(i.isupper()):
        upp_count+=1
    if(i.islower()):
        low_count+=1
print(f'The Upper count in the {str} is {upp_count}')
print(f'The Lower count in the {str} is {low_count}')