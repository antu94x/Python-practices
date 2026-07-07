a=int(input("Enter the tringle first arm length ="))
b=int(input("Enter the tringle second arm length ="))
c=int(input("Enter the tringle third arm length ="))
if a+b>c and b+c>a and c+a>b:
    print("Tringle possible")
else:
    print("Tringle not possible")