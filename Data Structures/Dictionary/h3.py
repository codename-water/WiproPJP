thisDic={}
n=int(input("Enter the number of entries you want in the dictionary."))

i=0
while i<n:
    a=input("Key")
    b=input("Value")
    thisDic[a]=b
    i+=1
    
print("Dictionary...",thisDic)

x=input("Enter the key you want to search.")

if x in thisDic:
    print(x,"is present in the Dictionary.")
else:
    print(x,"is not present in the Dictionary.")
