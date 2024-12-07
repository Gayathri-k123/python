colors=input("Enter colors separated by commas :")
colorlst=colors.split(",")
for i in range(len(colorlst)):
        colorlst[i]=colorlst[i].strip()
firstclr=colorlst[0]
lastclr=colorlst[-1]
print(f"First color = {firstclr}\nLast color = {lastclr}")
