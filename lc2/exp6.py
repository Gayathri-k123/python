names=input("Enter the first names seprated by space :").split()
a_count=0
for name in names:
        a_count+=name.lower().count('a')
print(f"The letter 'a' appears {a_count} times in the list of names")
