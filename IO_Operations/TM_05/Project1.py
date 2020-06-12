f1=open('file.txt')
num_lines=0
for i in f1:
    num_lines+=1
    
if num_lines<13:
    time=num_lines
    print('Time:%d AM'%(time))
elif num_lines<25:
    time=num_lines-12
    print('Time:%d PM'%(time))
f1.close()

f=open('file.txt')
str=f.read()
f.close()
words=str.split()
my_set=set(words)
max=0
place=None
for j in my_set:
    n=words.count(j)
    if max<n:
        max=n
        place=j

print('Place:%s Street'%(place.capitalize()))