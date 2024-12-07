n=int(input("Enter a limit:"))
l=[]
for i in range(1,n+1):
        if i%6==0 and i%4!=0:
                l.append(i)
print("List of integers divisible by 6 and not divisible by 4 upto this limit :",l)
s=0
for i in l:
        s=s+i;
print("Sum of these integers :",s)

