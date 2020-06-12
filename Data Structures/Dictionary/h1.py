thisDic={}
n=int(input("Enter the number of entries you want in the dictionary."))

i=0
while i<n:
    a=input("Key")
    b=input("Value")
    thisDic[a]=b
    i+=1
    
print(thisDic)

print("Enter a new Key and Value pair...")
a=input('Key')
b=input('Value')
thisDic[a]=b

print("Updates Dictionary...",thisDic)
