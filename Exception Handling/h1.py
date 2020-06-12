a=int(input('Enter first number...'))
b=int(input('Enter second number...'))
try:
    c=a/b
except:
    print('Exception occured.')
else:
    print('Result=%f'%(c))