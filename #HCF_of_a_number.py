#HCF_of_a_number
num1=int(input("Enter a Number1:"))
num2=int(input("Enter a Number2:"))
big=num1 if(num1>num2) else num2
small=num1 if(num1<num2) else num2
def check(big,small):
    rem=big%small
    if(rem==0):
        return(small)
    else:
       return(check(small,rem))  
    
result=check(big=big,small=small)
print(f'HCF of ({num1},{num2}) is:{result}')