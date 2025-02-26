#largest_in_an_array.py
import array
arr=array.array('i',[1,2,3,4,5])
big=arr[0]
for i in arr:
    if(big<i):
        big=i
print(f'the biggest element in the array :{arr.tolist()} is {big}')#here tolist s used to print the array in the list format by avoiding the typecode also 