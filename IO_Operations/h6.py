f1=open('sample4.txt')
str=f1.read()
f1.close()

thisList=str.split()
thisSet=set(thisList)

for i in thisSet:
    print('%s  ->  %d'%(i,thisList.count(i)))