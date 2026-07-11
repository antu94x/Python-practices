n=int(input("Enter a number for subcrescentic sequence="))
m=n
#using while loop
print("using while loop :")
while n>=1:
    print(n,end=" ")
    n-=1
    
#using for loop   
 
print("")
print("using for loop :")
for i in range(m,0,-1):
    print(i,end=" ")