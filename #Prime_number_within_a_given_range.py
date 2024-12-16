#Prime_number_within_a_given_range
lower_bound=int(input("Enter the Lower Range:"))
upper_bound=int(input("Enter the Upper Range:"))
for i in range(lower_bound,upper_bound+1):
    for j in range(2,i//2+1):
        if(i%j==0):
            break
    else:
        print(i)