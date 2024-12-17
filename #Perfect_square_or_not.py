#Perfect_square_or_not
#perfect number means whose square should be a integer
import math
num=int(input("Enter a Number:"))
if(math.floor(math.sqrt(num))==math.ceil(math.sqrt(num))):
    print("Perfect Square!")
else:
    print("Not Perfect Square!")