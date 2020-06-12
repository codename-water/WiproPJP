thislist=[]
n=int(input("Enter the number of elements you want to input."))

i=0
print("Enter the elements...")
while i < n:
    a=(input())
    thislist.append(a)
    i+=1

print("List is...",thislist)

a=input("Enter the element you want to append at the end of this list.")

thislist.append(a)

print("List after adding the element...",thislist)
