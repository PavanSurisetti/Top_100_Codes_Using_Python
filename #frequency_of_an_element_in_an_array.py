#frequency_of_an_element_in_an_array
import array
a=array.array('i',[10,9,10,9,8])
fcount={}
for i in a:
    count=0
    for j in a:
        if(i==j):
            count+=1
    if(i  not in fcount):#if it is there it will not add in doictionary
        fcount[i]=count
for i,j in fcount.items():#for displaying in a format
    print(f'{i}->{j}')