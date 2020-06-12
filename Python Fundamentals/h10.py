a=int(input("I/P:"))

ori=a
rev=0
while a>0:
    rev=(rev*10)+a%10
    a//=10

if rev==ori:
    print(ori,"is a palindrome.")
else:
    print(ori,"is not a palindrome.")
