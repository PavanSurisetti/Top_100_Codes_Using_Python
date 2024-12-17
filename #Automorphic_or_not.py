#Automorphic_or_not
#automorphoic means whose square of last digits[based on count] is equals to its original number 
num=(input("Enter a Number:"))
digits=len(num)
sq=str(int(num)**2)
lastdigits=sq[-digits:]
if(lastdigits==num):
    print("Automorphic Number!")
else:
    print("Not Automorphic Number!")
