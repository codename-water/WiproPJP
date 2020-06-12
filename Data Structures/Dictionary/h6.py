thisDic={}

n=int(input("Enter the number of values you want to input in Dictionary."))

i=0
print("Enter the keys and Values(Values must be integer)...")
while i<n:
    a=input("Key")
    b=int(input("Value"))
    thisDic[a]=b
    i+=1
    
print("Dictionary...",thisDic)

res=0
for k in thisDic:
    res+=thisDic[k]
    
print("Addition of all values is...",res)