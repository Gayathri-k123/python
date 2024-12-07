n=int(input("\nEnter the number of terms :"))
print(f"Fibonacci series of {n} terms : ")
a,b=0,1
print(a,b,end=" ")
for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a,b=b,c
print("\n")
