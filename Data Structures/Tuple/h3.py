thisList=[]

n=int(input('Enter the number of elements you want to input in the list.'))

print('Enter the elements of the list.')
i=0
while i<n:
    a=input()
    thisList.append(a)
    i+=1
    
print('List...',thisList)

thisTup=tuple(thisList) #Here we are converting the List into a tuple

print('Tuple formed is...',thisTup)