#HCF_Using_recursion
n1=int(input("Enter Number1:"))
n2=int(input("Enter Number2:"))
def Hcf(n1,n2):
    if(n2==0):#if n2 is zero then it returns n1
        return(n1)
    else:
        return(Hcf(n2,n1%n2))
print(f'The HCF of two Numebers ({n1},{n2}):{Hcf(n1,n2)}')      