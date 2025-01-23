#Number_of_days_in_a_month
month={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'october',11:'November',12:'December'}
user_month=int(input(f"Enter a Month \n {month}:"))
year=int(input("Enter a Year:"))
if(user_month==1 or user_month==3 or user_month==5 or user_month==7 or user_month==8 or user_month==10 or user_month==12):
    days=31
elif(user_month==2):#for february
    if(year%4==0 and (year%100!=0  or year%400==0)):#leap year
        days=29
    else:#not a leap year
        days=28
else:
    days=30#for all remainig months
print(f'The Number of Days in {month[user_month]} is :{days}')
