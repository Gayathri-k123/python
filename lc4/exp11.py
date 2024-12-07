import math 
a=float(input("Enter the first number:")) 
b=float(input("Enter the second number:")) 
c=float(input("Enter the third number:")) 
d=(b*b)-(4*a*c) 
if d==0: 
root=-b/2*a 
print(f"Real and equal roots:{root}") 
elif d>0: 
ans1=(-b-math.sqrt(d))/(2*a) 
 	ans2=(-b+math.sqrt(d))/(2*a) 
 	print(f"Real and distinct roots:{ans1} {ans2}") 
else: 
 	re=-b/2*a 
img=math.sqrt(abs(d))/(2*a) 
	print(f"Complex and distinct roots:{re}+{img}j") 
