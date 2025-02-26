#minimum_and_maximum_of_array
import array
arr=array.array('i',[1,2,3,4,5,6,7,8,9,10])
minval=arr[0]
maxval=arr[0]
for i in arr:
    if(minval>i):
        minval=i
    if(maxval<i):
        maxval=i
print(f'the minimum and maximum in the array :{arr.tolist()} is {minval} and {maxval}')