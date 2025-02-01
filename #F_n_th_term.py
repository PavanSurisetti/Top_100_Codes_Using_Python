#F_n_th_term
n=int(input("Enter a Number:"))#Taking input from the user 
start=1#for every it starts with 1
product=0#initially the product is zero
sum=0#initially the sum is zero 
for i in range(1,n+1):#it starts from one to desired user input  
    product=1#for every each iteration
    for j in range(i):#here it iterates upto the nth term multiplication
        product*=start
        start+=1
    sum+=product#1
print(sum)