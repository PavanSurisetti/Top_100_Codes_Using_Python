#max_palindorme_in_an_array
import array
ar1=array.array('i',[121,123454321,56765,456787654])
max_plaindorme=ar1[0]
for i in ar1:
    if(i>max_plaindorme):
        max_plaindorme=i
print(max_plaindorme)