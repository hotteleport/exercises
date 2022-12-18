import math
A = input("What is A? ")
A = int(A)
B = input("What is B? ")
B = int(B)

C = math.sqrt(A ** 2 + B **2)
C = "Volume of triangle is {} m3".format(round(C, 2))
print(C)