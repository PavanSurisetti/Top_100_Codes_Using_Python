#Capitalize_first_and_last_character
str=input("Enter a word:").split()
new_str=''
for q in str:
    for  i in range(len(q)):
        if(i==0 or i==len(q)-1):
            new_str+=q[i].upper()
        else:
            new_str+=q[i]
    new_str+=' '
print(f'After Capitalizing:{new_str}')