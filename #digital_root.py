#digital_root
''' digital root of a number is the single-digit value obtained by repeatedly summing its digits until only one digit remains. 
It is also known as the repeated sum of digits.'''
num=input("Enter a Number:")
sum=0
if(len(num)==1):
    print(int(num))
else:
    def repeat_sum(num):#this is a function which calculates recursively
        num=str(num)
        sum=0#everytime the sum starts from zero
        for i in num:
            sum+=int(i)
        if(len(str(sum))==1):
            print(sum)
        else:
            repeat_sum(sum)#if not a single digit then calculates again
    repeat_sum(num)