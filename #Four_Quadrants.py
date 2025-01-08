#Four_Quadrants
x=int(input("Enter the co-ordinate for 'X':"))
y=int(input("Enter the co-ordinate for 'Y':"))
'''x=0 and y=0->origin
   x>0 and y>0->first qaudrant
   x<0 and y>0->second quadrant
   x<0 and y<0->third quadrant
   x>0 and y<0->fourth quadrant'''
if(x==0 and y==0):
    print(f'The ({x},{y}) lies in Origin')
elif(x!=0 and y==0):
   print(f'The ({x},{y}) lies On X-Axis ')
elif(x==0 and y!=0):
   print(f'The ({x},{y}) lies On Y-Axis ')
else:
    if(x>0):
     if(y>0):
          print(f'The ({x},{y}) lies in Quadrant "Q1" ')
     else:
        print(f'The ({x},{y}) lies in Quadrant "Q4" ')
    else:
     if(y>0):
        print(f'The ({x},{y}) lies in Quadrant "Q2" ')
     else:
        print(f'The ({x},{y}) lies in Quadrant "Q3" ')