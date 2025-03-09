#checking_whether_it_is_anagram_or_not
str1=input("Enter a String1:")
str2=input("Enter a String2:")
str1_count={}#forming the dictionary for string1
str2_count={}#forming the dictionary for string2
if(len(str1)!=len(str2)):
        print("Not Anagram")
else:
    for i in str1:
        count=0
        for  j in str1:
            if(i==j):
                count+=1
        str1_count[i]=count
    for i in str2:
        count=0
        for j in str2:
            if(i==j):
                count+=1
        str2_count[i]=count
    if(str1_count==str2_count):#comparing whether the key and values are equals,if  then print Anagram
        print("Anagram")
    else:#if not then print Not Anagram
        print("Not Anagram")