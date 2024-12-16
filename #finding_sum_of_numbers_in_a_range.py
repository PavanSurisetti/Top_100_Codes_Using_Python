#finding_sum_of_numbers_in_a_range
low=int(input("Enter the Low Range:"))
high=int(input("Enter the High Range:"))
sum=0
for i in range(low,high+1):
    sum+=i
print(sum)