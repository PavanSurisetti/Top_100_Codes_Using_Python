#Harshad_number
#harshad number means  number  is divisble by sum of digits
num=int(input("Enter a Number:"))
def sum_of_digits(n):
    sum=0
    while(n!=0):
        rem=n%10
        sum+=rem
        n//=10
    return(sum)
result=sum_of_digits(num)
if(num%result==0):
    print("Harshad Number!")
else:
    print("Not Harshad Number!")
