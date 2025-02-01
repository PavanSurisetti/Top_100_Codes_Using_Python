#LCM_Using_recursion
n1=int(input("Enter Number1:"))
n2=int(input("Enter Number2:"))
def gcd(n1,n2):
    if(n2==0):
        return(n1)
    else:
        return(gcd(n2,n1%n2))
def lcm(n1,n2):
    return(n1*n2)//gcd(n1,n2)
print(f'The LCM of ({n1},{n2}) is :{lcm(n1,n2)}')