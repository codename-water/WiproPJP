def prime(n):
    flag=0
    for i in range(2,9n):
        if(n%i==0):
            flag=1
            break
    
    if flag==0:
        print(n,'is a prime number.')
    else:
        print(n,'is not a prime number.')


n=int(input('Enter a number...'))
prime(n)