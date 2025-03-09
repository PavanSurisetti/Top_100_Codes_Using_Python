#finding_non_repeating_characters_in_a_str
str=input("Enter a string:").lower()#storing the string
count_val={}#this is for storing the character count 
for i in str:
    count=0
    for j in str:
        if(i==j):
            count+=1#if it macthes then incrementing the count
    count_val[i]=count#adding each element into the dictionary
for x,y in count_val.items():#looping through the dictionary
    if(y==1):#if the count is exactly once then prinitng
        print(x,'',end='')