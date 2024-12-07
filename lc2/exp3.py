str1=input("Enter the first string :")
str2=input("Enter the second string :")
newstr1=str1[0]+str2[1]+str1[2:]
newstr2=str2[0]+str1[1]+str2[2:]
print(f"New string : {newstr1} {newstr2}")
