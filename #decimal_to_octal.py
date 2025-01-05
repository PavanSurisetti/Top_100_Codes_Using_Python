#decimal_to_octal
deci_num=int(input("Enter a Number:"))
octal_num=''
num=deci_num
while(num>0):
    rem=num%8
    octal_num=str(rem)+octal_num
    num=num//8
print(f'The octal form of {deci_num} is:{octal_num}')