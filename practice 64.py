#while loop
num=int(input("Enter a number ="))
i=1
total=0
while i<=num:
    total+=i
    i+=1
print("Using while loop =",total)

#for loop
Total=0
for i in range (1,num+1):
    Total+=i
print("Using for loop =",Total)