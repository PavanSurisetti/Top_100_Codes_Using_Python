#perfect_or_not
'''Perfect means sum of it's factors equals to its self [excluding itslef as a factor]'''
num=int(input("Enter a Number:"))
sum=0
for i in range(1,num//2+1):
    if(num%i==0):
        sum+=i
if(num==sum):
    print("Perfect Number!")
else:
    print("Not Perfect Number!")
    
