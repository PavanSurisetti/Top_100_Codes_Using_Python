#maximum_number_of_handshakes
def handshake(n):
    return(n*(n-1)//2)
n=int(input("Enter the Number of People:"))
print(f'The maximum number of Handshakes are :{handshake(n)}')