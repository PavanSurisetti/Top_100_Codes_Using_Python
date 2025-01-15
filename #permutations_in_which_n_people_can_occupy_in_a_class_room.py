#permutations_in_which_n_people_can_occupy_in_a_class_room
'''NpR=N!/(N-R)!'''
def factorial(x):
    fact=1
    if(x==1 or x==0):
        fact=1
    else:
        for i in range(1,x+1):
            fact=fact*i
    return(fact)
N=int(input("Enter the total number of students:"))
R=int(input("Enter the number of available seats:"))
print(f'The Total Possible Arrangements are:{factorial(N)//factorial(N-R)}')