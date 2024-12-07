colorlst1=input("Enter colors for list 1 ,separated by spaces:").split()
colorlst2=input("Enter colors for list 2 ,separated by spaces:").split()
unique_colors=[]
for color in colorlst1:
        if color not in colorlst2:
                unique_colors.append(color)
print("colors in list 1 not in lsit 2 :",unique_colors)
