thisSet=set()

n=int(input('Enter the number of elements you want to input in this set.'))

i=0
while i<n:
    a=input()
    thisSet.add(a)
    i+=1
    
print('Set...',thisSet)

a=input('Enter the element you want to remove from the set.')

thisSet.remove(a)

print('Set after removing',a,'is...',thisSet)
