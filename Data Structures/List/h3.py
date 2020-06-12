thislist=[]
n=int(input("Enter the number of elements you want to input."))

i=0
print("Enter the elements...")
while i < n:
    a=(input())
    thislist.append(a)
    i+=1

print("List before reversel...",thislist)

thislist.reverse()

print("List after reversel...",thislist)

