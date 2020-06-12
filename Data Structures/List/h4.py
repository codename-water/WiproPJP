thislist=[]
n=int(input("Enter the number of elements you want to input."))

i=0
print("Enter the elements...")
while i < n:
    a=(input())
    thislist.append(a)
    i+=1

print("List entered is...",thislist)

a=input("Enter the element you want to look for...")

n=thislist.count(a)

print(a,"has occured",n,"times in the list.")

