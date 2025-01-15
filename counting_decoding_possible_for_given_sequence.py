#counting_decoding_possible_for_given_sequence
sequence=input("Enter a Sequence:")
l=len(sequence)
count=0
for i  in range(l):
    t=int(sequence[i])#extracting ith digit value
    if(t>=1 and t<=9):
        if(count==0):#count all the single digit combinations as one 
         count+=1
    if(i+1<l):
        temp=(sequence[i:i+2])#two dgit checking
        if(  int(temp)>=10 and int(temp)<=26):
            count+=1  
print(f'The Possible sequence for the {sequence} is {count}')