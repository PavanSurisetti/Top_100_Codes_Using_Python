#octal_to_binary
octal_num=int(input("Enter a Number:"))
deci_num=0
num=octal_num
base=1
while(num>0):
    rem=num%10
    deci_num+=rem*base
    num=num//10
    base*=8
bin_num=''
temp=deci_num
while(temp>0):
    rem=temp%2
    bin_num=str(rem)+bin_num
    temp=temp//2
print(f'The Binary form of {octal_num} is {bin_num}')
