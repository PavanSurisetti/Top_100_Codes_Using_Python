#remove_duplicates_in_an_array
import array
a=array.array('i',[1,2,2,3,3,4,5,6,7])
unique_list=[]
for i in a:
    if i not in unique_list:
        unique_list.append(i)
unique_array=array.array('i',unique_list)
print(f'Before remvoing the duplicates:{a.tolist()}')
print(f'After removing the duplicates:{unique_array.tolist()}')