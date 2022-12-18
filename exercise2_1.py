import math
leigthA = input("What is A? ")
leigthA = int(leigthA)
leigthB = input("What is B? ")
leigthB = int(leigthB)
leigthC = input("What is C? ")
leigthC = int(leigthC)

V = leigthA * leigthB * leigthC
V = "Volume is {} m3".format(round(V, 2))
print(V)

r = input("What is radius? ")
r = int(r)
V = (4/3) * math.pi * (r ** 3)
V = "Volume of the sphere is {} m3".format(round(V, 2))
print(V)