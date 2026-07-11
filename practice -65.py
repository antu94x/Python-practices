#Using while loop Sum of even no 1 to "N"

N=int(input("Enter N ="))

#while loop
total=0
i=2
while i <= N:
    total+=i
    i+=2
print("Using while loop Sum of even no 1 to",N,"=",total)   

#for loop

Total=0

for i in range(2,N+1,2):#start,stop,step
    Total+=i
print("Using for loop Sum of even no 1 to",N,"=",Total)