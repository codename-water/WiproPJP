print("1. How much does it cost to operate one server per day?")
print("2. How much does it cost to operate one server per week?")
print("3. How much does it cost to operate one server per month?")
print("4. How many days can I operate one sever with $918?")

a=int(input("Select a query from above..."))

if a==1:
    print("Per day operation cost of a server is $",24*0.15)
    
elif a==2:
    print("Operation cost of a server for a week is $",7*24*0.15)
    
elif a==3:
    print("Operation cost of a server for a month is $",30*7*24*0.15)
    
else:
    print("You can oprate a server for",918//(0.15*24),"days with $918")