#smallest_element_in_array_using_recursion
import array #for performing operations on arrays
array1=array.array('i',[1, 4, 3, -5, -4, 8, 6])
def smallest(arr,n):
    if(n==1):
        return(arr[0])
    else:
        return min(arr[n-1],smallest(arr,n-1))
print(f'The Smallest in the Array is :{smallest(array1,len(array1))}')