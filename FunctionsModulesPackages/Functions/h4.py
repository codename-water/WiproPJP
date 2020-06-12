def count(string):
    countU=0
    countL=0
    
    for i in string:
        if i.isupper() and i!=' ':
            countU+=1
        elif i!=' ':
            countL+=1
    
    print('Number of  upper case letters in the string is...',countU)
    print('Number of  lower case letters in the string is...',countL)

    
string=input('Enter a string...')
count(string)