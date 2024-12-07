str=input("Eneter a string which has reocurence of first charecter :")
first_char=str[0]
new_str=first_char+str[1:].replace(first_char,'$')
print("New string : ",new_str)
