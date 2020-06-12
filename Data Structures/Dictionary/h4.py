thisDic={}
n=int(input("Enter the number of entries you want in the dictionary."))

i=0
while i<n:
    a=input("Key")
    b=input("Value")
    thisDic[a]=b
    i+=1
    
print("Keys...")
for k in thisDic:
    print(k)

print("Values...")
for k in thisDic:
    print(thisDic[k])

print("Key and their corresponding values...")
for k in thisDic:
    print(k,"->",thisDic[k])