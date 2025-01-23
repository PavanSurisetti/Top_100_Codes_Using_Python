#number_of_digits_in_a_number
num=int(input("Enter a Number:"))
temp=num
digit_count=0
while(num>0):
    rem=num%10
    digit_count+=1
    num=num//10
print(f'The Number of Digits in {temp} is {digit_count}')