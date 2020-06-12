def ispalindrome(name):
    rev=''
    for i in name:
        rev=i+rev
    if(rev==name):
        print('Yes, it is a palindrome.')
    else:
        print('No, it is not a palindrome.')

    
def count_the_vowels(name):
    count=0
    vowles='aeiou'
    for i in name:
        if i in vowles:
            count+=1
    print('No. of vowles:',count)
    
def frequency_of_letters(name):
    freq={}
    for i in name:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print('Frequency of characters is...',end=' ')
    for i in freq:
        print(i,'-',freq[i],', ',end='')
