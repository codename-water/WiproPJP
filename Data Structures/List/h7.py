n=int(input("Enter the nuber of elements you want to enter in the list."))

thisList=[]

i=0
while i<n:
    a=input()
    thisList.append(a)
    i+=1
    
print("List...",thisList)

a=int(input("Enter the position from where you want to remove the element."))

thisList.pop(a)

print("List after removing the element...",thisList)