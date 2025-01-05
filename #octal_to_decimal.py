#octal_to_decimal
octal_num=int(input("Enter a Number:"))
deci_num=0
num=octal_num
base=1
while(num>0):
    rem=num%10
    deci_num+=rem*base
    base*=8
    num=num//10
print(f'The decimal form of {octal_num} is:{deci_num}')