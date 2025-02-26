#sum_of_array_elements
import array
arr = array.array('i',[10, 89, 9, 56, 4, 80, 8])
sum=0
for i in arr:
    sum+=i
print(f'The sum of the array elements {arr.tolist()} is {sum}')