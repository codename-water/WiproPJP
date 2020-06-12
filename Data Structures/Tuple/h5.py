thisList=[(10, 20, 40), (40, 50, 60), (70, 80, 90)] 

print('Original List is...',thisList)
i=0
while i<3:
   a=thisList[i]
   b=list(a)
   b[2]=100
   a=tuple(b)
   thisList[i]=a
   i+=1

print('Updates List is...',thisList)