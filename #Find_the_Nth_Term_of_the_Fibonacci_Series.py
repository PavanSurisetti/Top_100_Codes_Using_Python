#Find_the_Nth_Term_of_the_Fibonacci_Series
num1=0
num2=1  
n=int(input("Enter a n th term:"))
if(n==1):
    print(num1)
elif(n==2):
    print(num2)
else:
    for i in range(2,n):
        num3=num1+num2
        num1=num2
        num2=num3
    print(num2)