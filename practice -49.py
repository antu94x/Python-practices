a=int(input("Enter the first number ="))
b=int(input("Enter the first number ="))
c=int(input("Enter the first number ="))

if a<b and a<c :
    print(a,"is smallest")
elif b<c and b<a:
    print(b,"is smallest")
else:
    print(c,"is smallest")