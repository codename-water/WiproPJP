from sys import argv

list1=argv[1].split("-")
list2=argv[2].split('-')
mainList=argv[3].split('-')

count=0

for i in mainList:
    if i in list1:
        count+=1
    elif i in list2:
        count+=-1
    
print(count)

