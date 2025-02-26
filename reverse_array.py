#reverse_array
import array
arr1=array.array('i',[1,2,3,4,5,6,7,8,9,10])#original array
print(f'Before Reversing the array:{arr1.tolist()}')#before reversing 
arr1=arr1[::-1]#slicing
print(f'After Reversing the array:{arr1.tolist()}')#after reversing