thisString=input('Enter a string...')

thisList=thisString.split()

count=0
for i in thisList:
    if (i.find('Alex')!=-1):
        count+=1
    elif (i.find('alex')!=-1):
        count+=1

print(count)