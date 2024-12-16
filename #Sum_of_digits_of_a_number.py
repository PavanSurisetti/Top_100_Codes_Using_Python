#Sum_of_digits_of_a_number.py
num=int(input("Enter a Number:"))
sum=0
while(num!=0):
    rem=num%10
    num=num//10
    sum+=rem
print(sum)