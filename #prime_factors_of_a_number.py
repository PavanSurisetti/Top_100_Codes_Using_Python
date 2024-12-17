#prime_factors_of_a_number
num=int(input("Enter a Number:"))
def prime(n):
    if(n<=1):
        return(False)
    else:
        for i in range(2,n//2+1):
            if(n%i==0):
                return(False)
        else:
            return(True)
for i in range(2,num//2+1):
    if(num%i==0):
       if(prime(i)):
            print(i,' ',end='')