#Reaplacing_all_zero's_with_one's
number=int(input("Enter a Number:"))
l=[]
for i in str(number):
    if(i=='0'):
        l.append('1')
    else:
        l.append(i)
num=''
for i in l:
    num+=i
print(f'Before replacing NUmber:{number}\nAfter replacing  Number:{int(num)}')