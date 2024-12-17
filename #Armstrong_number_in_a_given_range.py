#Armstrong_number_in_a_given_range
lower_range=int(input("Enter the Lower Range:"))
upper_range=int(input("Enter the Upper Range:"))
for i in range(lower_range,upper_range+1):
    digit_count=len(str(i))
    sum_of_digits=0
    for j in str(i):
        sum_of_digits+=int(j)**digit_count
    if(sum_of_digits==int(i)):
        print(i)