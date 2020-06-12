myList=[1,-2,3,-4,5,-6,7,-8,9,-10]
a=int(input('Enter an index to check the number in the list...'))
try:
    if myList[a]<0:
        print('Number at this index is negative.')
    else:
        print('Number at this index is positive.')
except:
    print('Please enter a valid index number.')