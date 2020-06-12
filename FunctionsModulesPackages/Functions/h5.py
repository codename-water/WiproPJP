def even(myList):
    flag=0
    tempList=[]
    for i in myList:
        flag=0
        if i%2==0:
            flag=1
            tempList.append(i)
            
    if(flag==0):
        print('There are no even numbers in this list.')
    else:
        print('Even digits in list are...',tempList)

        
myList=[]
n=int(input('Enter the number of digits you want to put int the list...'))
i=0
while i<n:
    a=int(input())
    myList.append(a)
    i+=1
even(myList)