#prime_number_using_recursion
number=int(input("Enter a Number:"))
def prime(n,i=2):
      if(n==i):
            return(True)
      else:
            if(n%i==0):
                  return(False)
            prime(n,i+1)
if(prime(number)):
      print(f'Yes,the {number} Is Prime Number')
else:
      print(f'No,the {number} Is  Not Prime Number')