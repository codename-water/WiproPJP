n=int(input("Enter the nuber of elements you want to enter in the list."))

thisList=[]

i=0
while i<n:
    a=input()
    thisList.append(a)
    i+=1
print("List...",thisList)

a=input("Enter the item you want to add to the list...")

thisList.insert(1,a)

print("List after adding the item in it...",thisList)