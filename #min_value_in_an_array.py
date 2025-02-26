#min_value_in_an_array
import array
arr=array.array('i',[1,2,3,4,56,7,-1])
minval=arr[0]
for i in arr:
    if(minval>i):
        minval=i
print(f'the smallest element in {arr.tolist()} is {minval}')