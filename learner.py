import math
a=int(input("Enter the Number"))
b=int(input("Enter the Number"))
c=int(input("Enter the Number"))
root= int(math.sqrt(4*a*c +b**2/2*a))
x=[int(-b + root/2*a), int(-b - root/2*a)]

print(x)