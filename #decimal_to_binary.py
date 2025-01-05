#decimal_to_binary
deci_num=int(input("Enter a Number:"))
bin_num=''
num=deci_num
if deci_num==0:
    bin_num='0'
while(num>0):
    rem=num%2
    bin_num+=str(rem) 
    num=num//2
bin_num=bin_num[::-1]
print(f'the binary form of :{deci_num} is :{bin_num}')
    