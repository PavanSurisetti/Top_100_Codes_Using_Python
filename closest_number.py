#Find the number closest to n and divisible by m
n=int(input("Enter a Number:"))
m=int(input("ENter a number:"))
quotient=n//m
lowclose=quotient*m
highclose=(quotient+1)*m
lowsub=n-lowclose
highsub=n-highclose
if(abs(lowsub)<abs(highsub)):
    print(f'closest is {lowclose}')
else:
     print(f'closest is {highclose}')