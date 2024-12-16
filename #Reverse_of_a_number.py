#Reverse_of_a_number
num=int(input("Enter a Number:"))
temp=num
rev=0
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(f"Reverse of {temp} is :{rev}")