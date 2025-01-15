#Addition_of_two_fractions
numerator1=int(input("Enter the Numerator1:"))
denominator1=int(input("Enter the denominator1:"))
numerator2=int(input("Enter the Numerator2:"))
denominator2=int(input('Enter the denominator2:'))
def fraction_sum(n1,d1,n2,d2):
    return(f'The sum of {n1}/{d1}+{n2}/{d2}:{((n1*d2)+(n2*d1))}/{(d1*d2)}')
print(fraction_sum(n1=numerator1,d1=denominator1,n2=numerator2,d2=denominator2))
    