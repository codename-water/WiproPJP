def nonblank_lines(f):      #function to ignore the blank lines while reading the file
    for l in f:
        line = l.rstrip()
        if line:
            yield line

#main program
name=input('Enter the name of the file...')
f=open(name+'.txt','r')

free=0
topay=0
paid=0
amount_paid=0
discount=0
for i in nonblank_lines(f):
    l=i.split()
    if 'Free' in l:
        free+=1
    elif 'Discount' in l:
        discount+=int(l[1])
    else:
        try:
            amount_paid+=int(l[0])
            topay+=1
        except:
            amount_paid+=int(l[1])
            topay+=1

f.close()
print('No. of items purchased:',topay)
print('No. of free items:',free)
print('Amount to pay:',amount_paid)
print('Discount given:',discount)
print('Final amount paid:',(amount_paid-discount))


