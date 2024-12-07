n=int(input("Enter a number : "))
f=1
if n<0:
        print("Factorial does not exist for negative numbers")
elif n==0 or n==1:
        print(f"Factorial of {n} is {f}")
else:
        for i in range(1,n+1):
                f=f*i
        print(f"Factorial of {n} is {f}")

