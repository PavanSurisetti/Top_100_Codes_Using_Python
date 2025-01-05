#HexaDecimal_to_Decimal
hexadeci_num=input("Enter a Number:").upper()
deci_num=0
base=1
num=hexadeci_num
keys={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
for rem in hexadeci_num[::-1]:
    if(rem  in keys):
         deci_num+=keys[rem]*base
    else:
        deci_num+=int(rem)*base
    base*=16
print(f'The decimal form of {hexadeci_num} is:{deci_num}')