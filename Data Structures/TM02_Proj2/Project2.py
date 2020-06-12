thisList=[]
n=int(input('Enter the number of elements in the list...'))

i=0
print('Enter the elements...')
while i<n:
    ele=int(input())
    thisList.append(ele)
    i+=1
    
thisList.sort()
m=thisList[-1]

i=-2
flag=0
while i>=-n:
    if thisList[i]<m:
        flag=1
        print('Second largest value in list is',thisList[i])
        break
    else:
        i-=1
        
if flag==0:
    print('All the values in the list are same.')
