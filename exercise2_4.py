import math
outside = input("kilometers outside urban area: ")
outside = int(outside)
within = input("kilometers within urban area: ")
within = int(within)

Consumption = (outside * 0.051) + (within * 0.075)
Consumption = "Consuption {} l".format(round(Consumption, 2))
print(Consumption)