a=int(input("Enter a Number. "))

flag=0
for i in range(2,a):
    if a%i==0:
        flag=1
        break

if flag==0:
    print("Number is Prime.")
else:
    print("Number is not-Prime.")
