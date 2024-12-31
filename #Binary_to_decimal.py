#Binary_to_decimal
num=(int(input("Enter a Number:")))
bin_num=num
deci_num=0
base=1
while(num>0):
    rem=num%10
    deci_num=deci_num+base*rem
    num=num//10
    base=base*2
print(f'Decimal Format of {bin_num} is:{deci_num}')