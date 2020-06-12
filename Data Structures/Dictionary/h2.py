thisDic1={}
n=int(input("Enter the number of entries you want in the dictionary 1."))

i=0
while i<n:
    a=input("Key")
    b=input("Value")
    thisDic1[a]=b
    i+=1

thisDic2={}
n=int(input("Enter the number of entries you want in the dictionary 2."))

i=0
while i<n:
    a=input("Key")
    b=input("Value")
    thisDic2[a]=b
    i+=1
    
thisDic3={}
n=int(input("Enter the number of entries you want in the dictionary 3."))

i=0
while i<n:
    a=input("Key")
    b=input("Value")
    thisDic3[a]=b
    i+=1
    
print("Dictionary 1...",thisDic1,"\n","Dictionary 2...",thisDic2,"\n","Dictionary 3...",thisDic3)

thisDic=thisDic1.copy()
thisDic.update(thisDic2)
thisDic.update(thisDic3)

print("Final Dictionary...",thisDic)