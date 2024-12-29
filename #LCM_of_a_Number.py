#LCM_of_a_Number
'''lcm can be caluculated by using the formula =(num1*num2)/hcf(num1,num2)'''
num1=int(input("Enter Number1:"))
num2=int(input("Enter Number2:"))
def hcf(num1,num2):
    big=num1 if(num1>num2) else num2
    small=num1 if(num1<num2) else num2 
    def check(big,small):
        rem=big%small
        if(rem==0):
            return(small)
        else:
            return(check(small,rem))
    result=check(big,small)
    return(result)
gcd=hcf(num1,num2)
lcm=(num1*num2)//gcd 
print(f'LCM of ({num1},{num2}) is:{lcm} ')