cents = input("Please enter how many cents do you have: \n")
cents = int(cents)

print(f"Amount of 50 cents: {cents // 50}")
cents = cents % 50
print(f"Amount of 25 cents: {cents // 25}")
cents = cents % 25
print(f"Amount of 10 cents: {cents // 10}")
cents = cents % 10
print(f"Amount of 5 cents: {cents // 5}")
cents = cents % 5
print(f"Amount of 2 cents: {cents // 2}")
cents = cents % 2
print(f"Amount of 1 cent: {cents}")