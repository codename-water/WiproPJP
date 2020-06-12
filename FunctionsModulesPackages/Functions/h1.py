def sumList(myList):
    s=0
    for i in myList:
        s+=i
    return s


n=int(input('Enter the number of values you want to input in the list...'))
myList=[]
i=0
while i<n:
    a=int(input())
    myList.append(a)
    i+=1   
print('Sum of all the values in the list is...',sumList(myList))