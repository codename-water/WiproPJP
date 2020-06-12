n=input('Enter a number...')
try:
    n=int(n)
except:
    print('Please enter a valid input.')
else:
    if n<0:
        print('Please enter a positive number.')
    else:
        i=2
        flag=1
        for i in range(2,n//2):
            if n%i==0:
                flag=0
                break
            else:
                i+=1
        if flag==1:
            print(n,'is a prime number.')
        else:
            print(n,'is not a prime number.')
    
    
