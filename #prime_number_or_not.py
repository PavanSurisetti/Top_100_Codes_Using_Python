#prime_number_or_not
num=int(input("Enter a Number:"))
if(num>1):
    for i in range(2,num//2+1):
        if(num%i==0):
            print("Not Prime Number!")
            break
    else:
     print("Prime Number!")
else:
   print("Not Prime Number!")