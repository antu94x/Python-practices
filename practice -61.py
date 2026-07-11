n=int(input("Enter a number for sequence counting ="))

print("using for loop :")

for i in range(1,n+1):
    print(i,end=" ")
print("")

print("using while loop :")
i=1
while i <= n:
    print(i,end=" ")
    i+=1