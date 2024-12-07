lst1=input("Enter a list of integers for list1 separated by spaces:").split()
l1=[]
for i in lst1:
        i.strip()
        l1.append(int(i))
lst2=input("Enter a list of integers for list2 separated by spaces:").split()
l2=[]
for i in lst2:
        i.strip()
        l2.append(int(i))
print("first List :",l1,"\nSecond List : ",l2)
print("(a)")
len1=len(l1)
len2=len(l2)
if len1==len2:
        print("The lists are of same length")
else:
        print("The lists are not same length")
print("(b)")
sum1=0
sum2=0
for i in l1:
        sum1+=i
for i in l2:
        sum2+=i
print("Sum of elements of first list:",sum1)
print("Sum of elements of second list :",sum2)
if sum1==sum2:
        print("The some of elements of both lists are equal")
else :
        print("The sum of elements of both lists are not equal")
print("(c)")
both_lst=[]
for i in lst1:
        if i in lst2:
                both_lst.append(i)
if both_lst:
        print("The value occurs in both lists are :")
        for i in both_lst:
                print(i)
else:
        print("There is no value occurs in both the lists")
