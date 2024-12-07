num=int(input("\nEnter a number:"))
num_str=str(num)
noofdigit=len(num_str)
sum=0
i=0
while i<noofdigit:
        n=int(num_str[i])
        p=n**noofdigit
        sum=sum+p
        i=i+1
if num==sum:
        print(f"{num} is an Armstrong number\n")
else:
        print(f"{num} is not an Armstrong number\n")
