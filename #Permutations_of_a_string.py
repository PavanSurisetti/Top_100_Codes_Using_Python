#Permutations_of_a_string
string=input("Enter a String:")
def permutations(str,answer=''):
    if(len(str)==0):
        print(answer)
    for i in range(len(str)):
        ch=str[i]   
        remaining=str[:i]+str[i+1:]
        permutations(remaining,ch+answer)
permutations(string)