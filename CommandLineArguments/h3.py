from sys import argv
from math import sqrt

def isprime(a):
    if a==1:
        return False
    flag=True
    for x in range(2, int(sqrt(a))+1):
        if a % x == 0:
            flag = False
            
    return flag

sum=0
for x in range(1,11) :
    i=int(argv[x])
    a=isprime(i)
    if a==True:
        sum+=i
        
print('Sum of all the prime numbers is...',sum)
    
