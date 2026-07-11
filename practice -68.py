#The sum of numbers between 1 to N divisible by 7.

N=int(input("Enter number for N ="))

total=0
#Using while loop

i=0
while i<=N:
    total+=i
    i+=7

print("Using while loop 1 to",N,"odd number sum =",total)

#Using for loop
Total=0
for i in range(0,N+1,7):
    Total+=i
    
print("Using for loop 1 to",N,"odd number sum =",Total)
