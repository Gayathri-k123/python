n=int(input("Enter a number:"))
l=[]
i=1
while(i<=n):
        if n%i==0:
                l.append(i)
        i=i+1
print(f"Factors of {n} are : {l}")
