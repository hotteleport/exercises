# ask a number of points
points = input("Give amount of points:\n")
points = int(points)
# terms
if 0 < points > 100:
    print("Invalid points value.")
if 0 <= points <= 50:
    print("Grate = 0")
if 51 <= points <= 60:
    print("Grate = 1")
if 61 <= points <= 70:
    print("Grate = 2")
if 71 <= points <= 80:
    print("Grate = 3")
if 81 <= points <= 90:
    print("Grate = 4")
if 91 <= points <= 100:
    print("Grate = 5")