a=int(input("I/P:"))

sum=0
while a>0:
    sum+=a%10
    a//=10

print('O/P:',sum)
