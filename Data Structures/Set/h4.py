thisSet=set()

n=int(input('Enter the number of elements you want to input in this set.'))

i=0
while i<n:
    a=input()
    thisSet.add(a)
    i+=1
    
print('Set...',thisSet)

print('Minimum in set is...',min(thisSet))
print('Maximum in set is...',max(thisSet))