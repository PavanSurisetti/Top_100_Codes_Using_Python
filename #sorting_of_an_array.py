#sort the elements of the array
import array
arr=array.array('i',[10,9,8,7,6,5,4,3,2,1])
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr.tolist())