#frequency_of_a_character_in_a_string
str=input('Enter a String:')
freq_count={}
for i in str:
    count=0
    for j in str:
        if (i==j):
            count+=1
    freq_count[i]=count
print(freq_count)