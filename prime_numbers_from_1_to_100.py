#prime_numbers_from_1_to_100
for i in range(2,101):
    for j in range(2,i+1//2):
        if(i%j==0):
            break
    else:
        print(i,' ',end='')