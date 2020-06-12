a=input('Enter a String...')

countL=0
countU=0
for c in a:
    b=c
    if b.isupper() and b!=' ':
        countU+=1
    elif b.islower() and b!=' ':
        countL+=1
        
print("Number of Upper Case Characters in string is...",countU)
print('Number of Lower Case Characters in string is...',countL)