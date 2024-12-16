#greatest_of_three_numbers
num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
num3=int(input("Enter the number3:"))
big=num1 if(num1>num2 and num1>num3) else num2 if(num2>num3) else num3
print(big)