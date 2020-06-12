thisDic={}
n=int(input('Enter the number of entries in the Dictionary...'))

i=0
while i<n:
    tempList=[]
    name=input('Enter the name of the Student...')
    j=0
    print('Enter the number of Subjects sequentially... 1. Maths, 2. Physics, 3. Chemistry')
    while j<3:
        a=float(input())
        tempList.append(a)
        j+=1
    thisDic[name]=tempList
    i+=1
    
print('Dictionary formed is...',thisDic)

name=input('Enter the full-name whose average marks you want to check...')
thisList=thisDic.get(name)
add=0
for i in thisList:
    add+=i

print('Average marks of',name,'are',add/3)
        