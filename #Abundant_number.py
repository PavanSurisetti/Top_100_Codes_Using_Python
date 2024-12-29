#Abundant_number
#abudant number means it's sum of divisors[excluding itself] should be greater than the original number
num=int(input("Enter a Number:"))
def finding_factors_sum(n):
    sum=0
    for i in range(1,n//2+1):
        if(n%i==0):
            sum+=i
    return(sum)
sum=finding_factors_sum(num)
if(sum>num):
    print("Abundant Number!")
else:
    print("Not Abundant Number!")
