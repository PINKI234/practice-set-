import math
a = flot(input("enter co-efficient of x^2:"))
b = flot(input("enter co-efficient of x:"))
c = flot(input("enter constant : " ))
alpha = (-b+math.sqrt (b**2-(4*a*c)))/(2*a)
bita  = (-b-math.sqrt(b**2-(4*a*c)))/(2*a)
print(alpha)
print(bita)
