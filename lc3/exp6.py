from math import *
n=int(input("\nEnter the limit:"))
prime=[]
for i in range(2,n+1):
        is_prime=True
        for j in range(2,int(sqrt(i))+1):
                if i%j==0:
                        is_prime=False
        if is_prime:
                prime.append(i)
print("Prime numbers:",prime)
print("Alternate prime  numbers:")
for i in range(0,len(prime),2):
        print(prime[i],end=" ")
print("\n")
