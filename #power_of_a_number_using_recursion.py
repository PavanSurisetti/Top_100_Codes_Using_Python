#power_of_a_number_using_recursion
def power(base,exp):
    if(exp==0):
        return(1)
    return(base*power(base,exp-1))
base=int(input("Enter The Base value:"))
exp=int(input("Enter The Exponential Value:"))
print(power(base,exp))