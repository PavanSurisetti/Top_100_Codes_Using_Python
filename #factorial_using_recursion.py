#factorial_using_recursion
n=int(input("Enter a Number:"))
def factorial(n):
    if(n==0 or n==1):
        return(1)
    else:
        return(n*factorial(n-1))
print(factorial(n))