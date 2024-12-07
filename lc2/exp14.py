print("(a)")
num=input("Enter a list of integers seperated by spaces:").split()
l=[]
for i in num:
        i=int(i)
        if i>0:
                l.append(i)
print("List of numbers containing only positive numbers : ",l)
print("\n(b)")
square=[]
n=int(input("Enter a limit to find the square of numbers:"))
for i in range(1,n+1):
        square.append(i**2)
print(f"List containing the square of first {n} numbers : {square}")
print("\n(c)")
word=input("Enter a word:")

vowel=[]
for i in word:
        if i in ['a','e','i','o','u']:
                vowel.append(i)
print(f"List of vowels selected from the word '{word}' is {vowel}")
print("\n(d)")
w=input("Enter a word : ")
ordinal=[]
for i in w:
        ordinal.append(ord(i))
print(f"List of ordinal value of each element of the word '{w}' is {ordinal}")
