f1=open('sample3.txt')
string=f1.read()
f1.close()
list_of_words=string.split()

max=len(list_of_words[0])
word=list_of_words[0]
i=0
while i<len(list_of_words):
    if max<len(list_of_words[i]):
        max=len(list_of_words[i])
        word=list_of_words[i]
    i+=1

print('Longest word in the file is...',word)