thisTup=(1, 2.25, 'a', 3, 'b', 'c', 4, 'd', 5, 6, 'e', 'f', 7)

print('Tuple...',thisTup)

a=input('Enter the element you want to search in tuple...')

if a in thisTup:
    print('Yes,',a,'is present in tuple.')
elif float(a) in thisTup:
    print('Yes,',a,'is present in tuple.')
else:
    print('No,',a,'is not present in tuple.1')