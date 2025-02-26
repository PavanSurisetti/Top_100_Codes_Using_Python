#even_count_and_odd_count_in_an_array
import array
array1=array.array('i',[11,20,35,40,53])
even_count=0
odd_count=0
for i in array1:
    if(i%2==0):
        even_count+=1#for checking the even code
    else:
        odd_count+=1#for checking the odd count
print(f'In {array1.tolist()} The even count is {even_count} and the odd count is {odd_count}')