#Occurence_of_a_specific_digit_in_a_number
number=(input("Enter a Number:"))
key=int(input("Enter The Key Digit:"))
count=0
for i in number:
    if(key==int(i)):
        count+=1
print(f'The {key} in {number} Occurs:{count}')