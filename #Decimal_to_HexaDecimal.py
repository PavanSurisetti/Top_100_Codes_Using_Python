#Decimal_to_HexaDecimal
decimal_num=int(input("Enter a Number:"))
hexa_deci=''
num=decimal_num
keys = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
while(num>0):
    rem=num%16
    if(rem in keys):
        hexa_deci=keys[rem]+hexa_deci
    else:
        hexa_deci=str(rem)+hexa_deci
    num=num//16
print(f'The HexaDecimal form of {decimal_num} is:{hexa_deci}')