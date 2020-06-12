list1=[]
list2=[]

a=int(input("Enter the number of elements you want to input in list one..."))
print("Enter list one...")
i=0
while i<a:
    x=input()
    list1.append(x)
    i+=1
    
b=int(input("Enter the number of elements you want to input in list two..."))
print("Enter list two...")
i=0
while i<b:
    x=input()
    list2.append(x)
    i+=1

print("List 1 :",list1)
print("List 2 :",list2)
    
i=0
while i<a:
    list2.insert(i,list1[i])
    i+=1
    
print("Lists after appending are...","List 1 :",list1,"; List 2 :",list2)
