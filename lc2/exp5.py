str=input("Enter a string :")
if "ing" in str:
        newstr=str[0:-3]+"ly"
else:
        newstr=str+"ing"
print("New string :",newstr)
