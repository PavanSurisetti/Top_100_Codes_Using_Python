#Can_a_number_expressed_as_a_sum_of_two_prime_number
num=int(input("Enter a Number:"))
def prime(n):
    set_of_prime=[]
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if(i%j==0):
                break
        else:
            set_of_prime.append(i)
    return(set_of_prime)
set_of_prime_numbers=prime(num)
print(set_of_prime_numbers)
found=False
for i in set_of_prime_numbers:
    if (num-i) in set_of_prime_numbers:
        print(f'{num} can be expressed as sum of {i} and {num-i}')
        found=True
        break
if not found:
        print(f'{num} cannot be expressed as the sum of two prime numbers')