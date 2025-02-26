#second_shortest_element_in_an_array
import array
arr=array.array('i',[10,9,8,7,6,5,4,3,2,1])
for i in range(0,len(arr)):
    if(i==len(arr)):
        break
    else:
        for j in range(0,len(arr)-1):
          if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(f'the second smallest element in {arr.tolist()} is {arr[1]}')