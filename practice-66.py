N=int(input("Enter number for odd numbers sum =",))

total=0
#Using while loop

i=1
while i<=10:
    total+=i
    i+=2

print("Using while loop 1 to",N,"odd numbers sum =",total)

#Using for loop
for i in range(1,N+1,2):
    total+=i
    
print("Using for loop 1 to",N,"odd numbers sum =",total)


