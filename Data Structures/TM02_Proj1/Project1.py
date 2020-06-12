myDictionary={}
n=int(input('Enter the number of inputs you want to put in the dictionary...'))
print('Enter the name of Person and then the interesting fact...')
i=0
while i<n:
    a=input('Name of person...')
    b=input('Interesting fact...')
    myDictionary[a]=b
    i+=1

print('Dictionary formed is...',myDictionary)

x=input('Enter the name of Person whose fact you want to change...')
if x in myDictionary:
    y=input('Enter the fact...')
    myDictionary[x]=y
else:
    print('This person is not in the dictionary.')

print('Updated dictionary after changing the fact about',x,'is...',myDictionary)

a=input('Enter the name of the person you want to add...')
b=input('Enter the interesting fact...')
myDictionary[a]=b
print('Updated dictionary after adding a new set is...',myDictionary)