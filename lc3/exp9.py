n=int(input("Enter a number:"))
s=str(n)
if s==s[::-1]:
        print("This Number is Palindrome")
else:
        print("This Number is not a Palindrome")
