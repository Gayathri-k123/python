n=int(input("\nEnter the number of elements :"))
l=[]
for i in range(n):
        a=int(input("Enter the element : "))
        l.append(a)
print("List : ",l)
sum=0
for i in l:
        sum=sum+i
print("Sum of elements : ",sum)

