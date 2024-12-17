#Factorial_of_a_number
num=int(input("Enter a Number:"))
fact=1
if(num==0):
    fact=1
else:
    for i in range(1,num+1):
        fact*=i
print(fact)