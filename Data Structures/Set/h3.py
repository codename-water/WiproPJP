thisSet1=set()

n=int(input('Enter the number of elements you want to input in this set.'))

i=0
while i<n:
    a=input()
    thisSet1.add(a)
    i+=1
    
thisSet2=set()

n=int(input('Enter the number of elements you want to input in this set.'))

i=0
while i<n:
    a=input()
    thisSet2.add(a)
    i+=1

print('Set 1...',thisSet1,'Set 2...',thisSet2)

thisSet3=thisSet1.union(thisSet2)
print('Union of set 1 and set 2 is',thisSet3)
