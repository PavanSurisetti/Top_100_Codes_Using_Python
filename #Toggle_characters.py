#Toggle_characters
str=input("Enter a String:")
toggle=''
for i in str:
    if(i.islower()):
        toggle+=i.upper()
    else:
        toggle+=i.lower()
print(f'The toggle of {str} is {toggle}')