#number_to_words
num=input("Enter a Number:")
single_digit={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
double_digit={1:'ten',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
exp_digit={10:'ten',11:'eleven',12:'twelve',13:'Thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
l=len(num)
if(l==0):
    print('Zero')
else:
    if(l==1):#for single digit numbers
        print(f'{num}:{single_digit[int(num)]}')
    elif(l==2):#for double digit numbers
        if(int(num[1])==0):
            print(f'{num}:{double_digit[int(num[0])]}')
        elif(int(num[0])==0):
            print(f'{num}:{single_digit[int(num[1])]}')
        elif(int(num) in exp_digit):
            print(f'{num}:{exp_digit[int(num)]}')
        else:
            print(f'{num}:{double_digit[int(num[0])]}  {single_digit[int(num[1])]}')
    elif(l==3):#for 3 digit numbers
            if(int(num[0])==0):#if the first digit is zero 
                if(int(num[2])==0):#if the last digit is zero
                    print(f'{num}:{double_digit[int(num[1])]}')
                elif(int(num[1])==0):#if the second digit is zero
                   print(f'{single_digit[(int(num[0]))]} Hundred {single_digit[(int(num[2]))]}')
                elif(int(num) in exp_digit):#if any exception cases like eleven
                 print(f'{num}:{exp_digit[int(num)]}')
                else:
                  print(f'{num}:{double_digit[int(num[1])]}  {single_digit[int(num[2])]}')
            else:
                if(int(num[1])==0 and int(num[2])==0 ):
                    print(f'{num}:{single_digit[int(num[0])]} Hundred')
                elif(int(num[2])==0):
                  print(f'{num}:{single_digit[int(num[0])]} Hundred {double_digit[int(num[1])]}')
                elif(int(num[1])==0):#if the second digit is zero
                   print(f'{num}:{single_digit[(int(num[0]))]} Hundred {single_digit[(int(num[2]))]}')
                else:
                    if(int(num[1])==1):
                     print(f'{num}:{single_digit[int(num[0])]} Hundred {exp_digit[int(num[1:])]}')
                    else:
                         print(f'{num}:{single_digit[int(num[0])]} Hundred {double_digit[int(num[1])]} {single_digit[(int(num[2]))]}')
    elif(l==4):#for 4 digit numebrs
        if(int(num[0])==0):#in 4 digit ,if the last digit is zero
            if( int(num[1])==0 and int(num[2])==0):#if the first three digits are zero
               print(f'{num}:{single_digit[(int(num[3]))]}') 
            elif(int(num[1])==0):#if the first ,two digits are zero's
               if(int(num) in exp_digit):#if it is in exception case digits
                   print(f'{num}:{exp_digit[(int(num))]}')
               else:
                  if(int(num[3])==0):
                     print(f'{num}:{double_digit[int(num[2])]}')
                  else:
                     print(f'{num}:{double_digit[int(num[2])]} {single_digit[(int(num[3]))]}')
            elif(int(num[2])==0):
               print(f'{num}:{single_digit[int(num[1])]} Hundred {single_digit[(int(num[3]))]}')
            elif(int(num[3])==0):#in case of last digit is zero 
             print(f'{num}:{single_digit[int(num[1])]} Hundred {double_digit[int(num[2])]}')
            elif(int(num[2:]) in exp_digit):#any exception case like eleven,etc....
             print(f'{num}:{single_digit[int(num[1])]} Hundred {exp_digit[int(num[2:])]}')
            
            else:#for regular numbers[not lst digit is zero]
               print(f'{num}:{single_digit[int(num[1])]} Hundred {double_digit[int(num[2])]} {single_digit[(int(num[3]))]}' )
        else:
            if(int(num[1])==0 and int(num[2])==0 and int(num[3])==0):
               print(f'{num}:{single_digit[int(num[0])]} Thousand')
            elif( int(num[1])==0 and int(num[2])==0):#if the hundred's and ten's place digits are zero
                print(f'{num}:{single_digit[(int(num[0]))]} Thousand {single_digit[int(num[3])]}')
            elif(int(num[1])==0):#if the hundreds digits is zero
               if(int(num[2:]) in exp_digit):#if it is in exception case digits
                   print(f'{num}:{single_digit[(int(num[0]))]}Thousand {exp_digit[(int(num[2:]))]}')
               else:
                  if(int(num[3])==0):
                     print(f'{num}:{single_digit[(int(num[0]))]} Thousand {double_digit[int(num[2])]}')
                  else:
                     print(f'{num}:{single_digit[(int(num[0]))]} Thousand {double_digit[int(num[2])]} {single_digit[int(num[3])]}')
            elif(int(num[1])!=0 and  int(num[2])!=0 and int(num[3])==0):#in case,if the last digit is zero
               print(f'{num}:{ single_digit[int(num[0])]} thousand {single_digit[int(num[1])]} Hundred {double_digit[int(num[2])]}')
            elif(int(num[2])==0):
               print(f'{num}:{single_digit[int(num[0])]} Thousand {single_digit[int(num[1])]} Hundred {single_digit[(int(num[3]))]}')
            else:
             if(int(num[3])==0):
                print(f'{num}:{ single_digit[int(num[0])]} thousand {single_digit[int(num[1])]} Hundred {double_digit[int(num[2])]}')
             elif(int(num[2:]) in exp_digit):
                 print(f'{num}:{single_digit[int(num[0])]} Thousand {single_digit[(int(num[1]))]} Hundred {exp_digit[int(num[2:])]}')
             else:
                 print(f'{num}:{ single_digit[int(num[0])]} thousand {single_digit[int(num[1])]} Hundred {double_digit[int(num[2])]} {single_digit[(int(num[3]))]}')
    else:
       pass