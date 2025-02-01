#length_of_string_using_recursion
string=input("Enter a String:")
global count
count=0
def length(str):
    if(str==''):
        return(0)
    else:
     return(1+length(str[1:]))
print(f'The Length of {string} is :{length(string)}')