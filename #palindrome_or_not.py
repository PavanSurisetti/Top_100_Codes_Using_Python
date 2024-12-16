#palindrome_or_not
num=int(input("Enter a Number:"))
temp=num
reverse=0
while(num!=0):
    rem=num%10
    reverse=reverse*10+rem
    num//=10
if(temp==reverse):
    print("Palindrome!")
else:
    print("Not Palindrome!")
