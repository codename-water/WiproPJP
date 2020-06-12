f1=open('sample2.txt','r')
list_of_lines=f1.readlines()
f1.close()

j=1
print('List of lines stored in a List...\n')
for i in list_of_lines:
    print('Line',j,'->',i)
    j+=1
