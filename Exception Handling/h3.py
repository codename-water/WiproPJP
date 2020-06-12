a=input('Enter the name of the file you want to open...')
try:
    f1=open(a,'r')
except:
    print('This file does not exist.')
else:
    print('Content of the file is...',f1.read())
    f1.close()