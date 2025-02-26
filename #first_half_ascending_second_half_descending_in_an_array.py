#first_half_ascending_second_half_descending_in_an_array
import array
arr=array.array('i',[5,4,3,2,1,10,12,13,14,15])
arr2=[]
for i in range(len(arr)//2):#for the first half we are changing into the ascending order 
    for j in  range(len(arr)//2-1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
for i in range(len(arr)//2,len(arr)):#for the second half we are changing it into the descendoing order
    for j in range(len(arr)//2,len(arr)-1):
        if(arr[j]<arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr.tolist())