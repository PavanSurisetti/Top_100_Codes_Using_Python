#finding_the_non_repeating_elements.py
import array
a=array.array('i',[10,20,70,90,80,20,10,20])
dfcount=[]
for i in a:
    if(a.count(i)==1):
         dfcount.append(i)
print(dfcount)