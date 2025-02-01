#reversing_a_number_using_recursion
num=input("Enter a Number:")
def reverse(num,n):
    if(n==1):
        return(num[0])
    else:
        return(num[n-1]+reverse(num,n-1))
print(f'The reverse of {num} is {reverse(num,len(num))}')