from math import sqrt
squares = []
ll = int(input("Enter the lower limit (1000-9999): "))
ul = int(input("Enter the upper limit (1000-9999): "))
if ll < 1000 or ul > 9999 or ll > ul:
    print("Please enter a valid range between 1000 and 9999.")
else:
        for i in range(ll, ul + 1):
                if sqrt(i) == int(sqrt(i)):
                        squares.append(i)
        print("Perfect squares between this limit:", squares)
        even = []
        for i in squares:
                square_str = str(i)
                if all(int(digit) % 2 == 0 for digit in square_str):  
                        even.append(i)
        print("Perfect squares between this limit with all digits even:", even)
