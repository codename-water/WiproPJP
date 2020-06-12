a=input('Enter a String...')
a=a.casefold()      #making it suitable for caseless comparison

b=''
for i in a:
    b=i+b

if (a==b):
    print('Yes, String is palindrome.')
else:
    print('No, String is not palindrome.')