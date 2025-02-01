#largest_element_in_array_using_recursion
import array
arr1=array.array('i',[1,2,3,5,6,7,8,12,3,-1,-3])#creating an array
def largest(arr,n):#function for finding the largest of the array
    if(n==1):#if the index is 1 then it returns the element from the index zero th position
        return(arr[0])
    else:
        return max(arr[n-1],largest(arr,(n-1)))#finding maximum among all the values 
print(f'The Largest in the array is:{largest(arr1,len(arr1))}')#function calling