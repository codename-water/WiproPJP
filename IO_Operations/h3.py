f1=open('sample1.txt','a')
a=input('Enter the text you want to add to the file...')
f1.write(a+'\n')
f1.close()
print('File updated...')
