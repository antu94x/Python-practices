N=int(input("Enter number for odd numbers sum =",))

total=0
#Using while loop

i=1
while i<=N:
    total+=i
    i+=2

print("Using while loop 1 to",N,"odd numbers sum =",total)

#Using for loop
Total=0
for i in range(1,N+1,2):
    Total+=i
    
print("Using for loop 1 to",N,"odd numbers sum =",Total)


