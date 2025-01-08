#binary_to_octal
bin_num=int(input("Enter a Number:"))
deci_num=0
base=1
num=bin_num
while(num>0):
    rem=num%10
    deci_num=(deci_num)+rem*base
    num=num//10
    base=base*2
oct_num=''
temp=deci_num#for storing the deci_num
octal_base=1
while(temp>0):
    rem_oct=temp%8
    oct_num=str(rem_oct)+oct_num
    temp=temp//8    
print(f'the octal form of {bin_num} is {oct_num}')