words=input("Enter a list of words seperated by spaces:").split()
l=[]
for word in words:
        l.append(word.strip())
print("The list of words is:",l)
max_len=0
for i in l:
        if len(i)>max_len:
                max_len=len(i)
print("Length of longest word: ",max_len)
