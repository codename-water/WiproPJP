a=input('Enter a string...')

b=a[:2]     #Extracting first two elements from the string
n=len(a)

i=1
while i<n:
    b=b+a[:2]
    i+=1

print("Resultant string...",b)