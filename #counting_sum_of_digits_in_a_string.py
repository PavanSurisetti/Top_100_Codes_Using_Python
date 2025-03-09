#counting_sum_of_digits_in_a_string
str=input("Enter a String:")
numbers=['1','2','3','4','5','6','7','8','9','0']
sum=0
for i in str:
    if i  in numbers:
            sum+=int(i)
print(f'Sum Of numbers in {str} is {sum}')