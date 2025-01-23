#Finding_Roots_of_a_Quadratic_Equation
import math
a=int(input("Enter The coefficient of a:"))#coefficient of x^2
b=int(input("Enter The coefficient of b:"))#coefficient of x
c=int(input("Enter The coefficient of c:"))#Constant
disc=b*b-4*a*c
if(disc==0):
    print("Roots Are Real and Equal")
    root1=root2=-b/2*a
elif(disc>0):
    print('Roots Are Real and Distinct')
    root1=(-b+math.sqrt(disc))/(2*a)
    root2=(-b-math.sqrt(disc))/(2*a)
else:
    print('Roots Are Imaginary and Complex')
    root1=(-b+math.sqrt(-disc))/(2*a)
    root2=(-b-math.sqrt(-disc))/(2*a)
print(f'Roots are Root1:{root1} Root2:{root2}')