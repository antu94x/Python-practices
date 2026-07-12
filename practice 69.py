N=int(input("Enter N ="))
#while loop
i=0
print("Using while loop",1,"to",N,"Divisible of 3 and 5 both are")
while i<=N:
    i+=3
    if i%3==0 and i%5==0:
         print(i,end=" ")
print( )
#using for loop
print("Using for loop",1,"to",N,"Divisible of 3 and 5 both are")
for i in range(3,N+1,3):
    if i%3==0 and i%5==0:
        print(i,end=" ")