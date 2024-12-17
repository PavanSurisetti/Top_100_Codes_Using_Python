#strong_number_or_not
num=int(input("Enter a Number:"))
sum=0
temp=num
def factorial(n):
    if(n==0 or n==1):
        return(1)
    else:
        return(n*factorial(n-1))
while(num!=0):
    rem=num%10
    num=num//10
    sum+=factorial(rem)
if(temp==sum):
    print("Strong Number!")
else:
    print('Not Strong Number!')