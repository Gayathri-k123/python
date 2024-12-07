from palin import ispalindrome
def longest(s):
        n=len(s)
        longest=" "
        for i in range(len(s)):
                for j in range(i+1,len(s)+1):
                        substring=s[i:j+1]
                        if ispalindrome(substring) and len(substring)>len(longest):
                                longest=substring
        return longest
txt=input("enter a string")
result=longest(txt)
print("longest string",result)


