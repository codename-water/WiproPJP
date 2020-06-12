a=input('Enter the string...')
n=int(input('Enter the value of \'n\'...'))

b=a[-n:]        #Extracting the Last 'n' digits from the strings

i=1
while i<n:
   b=b+a[-n:]
   i+=1

print('String obtained is...',b)

