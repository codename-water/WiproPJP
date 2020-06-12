def arrange(string):
    thisList=string.split('-')
    thisList.sort()
    string=''
    n=len(thisList)
    i=0
    while i<n-1:
        string+=thisList[i]
        string+='-'
        i+=1
    string+=thisList[n-1]
    return string
    

string=input('Enter the string...')
s=arrange(string)
print('The Sorted string is...',s)
