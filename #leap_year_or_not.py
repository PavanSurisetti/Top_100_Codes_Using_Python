#leap_year_or_not
year=int(input("Enter a Year:"))
check='Leap year!' if(year%4==0 and (year%400==0 or year%100!=0)) else 'Not Leap Year'
print(check)