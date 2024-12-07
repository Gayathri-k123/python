str=input("Enter a sting :")
c={}
for i in str:
        if i in c:
                c[i]+=1
        else:
                c[i]=1
print(c)
count=len(str)
print(f"The total number of charecters in the string '{str}' is {count}")
