#finding_the_repeating_elements.py
import array
a=array.array('i',[10,20,40,30,50,20,10,20])
dfcount=[]
for i in a:
    if(a.count(i)>=2):
        if(i not in dfcount):
         dfcount.append(i)
print(dfcount)