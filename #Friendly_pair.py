#Friendly_pair
num1=int(input("Enter  a Number1:"))
num2=int(input("Enter a Number2:"))
def factors_sum(n):
    sum=0
    for i in range(1,n//2+1):
        if(n%i==0):
            sum+=i
    return(sum)
sum1=factors_sum(num1)
sum2=factors_sum(num2)
ratio1=sum1/num1
ratio2=sum2/num2
if(ratio1==ratio2):
    print(f"({num1},{num2}) is a  Friendly Pair!")
else:
    print(f"({num1},{num2}) is not a Friendly Pair:!")
