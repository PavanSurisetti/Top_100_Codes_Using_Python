#sum of geometric series
a=int(input("enter the first term:"))
r=int(input("enter the common ratio:"))
n=int(input("Enter the number of terms:"))
if(r==1):
    sum=n*a
else:
    sum=(a*(1-r**n))/(1-r)
print(sum)