numbers=input("Enter a list of integers seperated by spaces :").split()
lst=[]
for i in numbers:
        lst.append(int(i))
print("List : ",lst)
m_lst=[]
for i in lst:
        if i%2!=0:
                m_lst.append(i)
print("Modified list : ",m_lst)
