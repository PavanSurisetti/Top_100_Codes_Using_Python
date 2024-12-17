#Armstrong_number
num=input("Enter a Number:")
digit_count=len(num)
sum=0
for i in num:
    sum+=int(i)**digit_count
if(int(num)==sum):
    print("Armstrong Number!")
else:
    print("Not Armstrong Number!")