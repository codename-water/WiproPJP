n=int(input('Enter the number of lines you want to read from the file...'))

f1=open('sample.txt','r')
i=0
j=1
print('First',n,' lines from the file are...\n')
while i<n:
    print('Line',j,'->',f1.readline())
    i+=1
    j+=1
f1.close()
    
    