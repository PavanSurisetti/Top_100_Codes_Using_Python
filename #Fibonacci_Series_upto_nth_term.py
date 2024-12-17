#Fibonacci_Series_upto_nth_term
num1=0
num2=1
n=int(input("Enter the nth term:"))
for i in range(1,n+1):
    print(num1,' ',end='')
    num3=num1+num2
    num1=num2
    num2=num3
