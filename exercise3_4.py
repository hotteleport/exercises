# ask info by user
money = input("Give money:\n ")
money = int(money)
cost = input("Purchase cost:\n ")
cost = int(cost)
# terms
if cost > money:
    give = cost - money
    give = int(give)
    print(f"Not enough money, give more: \n{give}")
    money = input("Give more money:\n ")
    money = int(money)
if cost > money:
    print("You do not have enough money\n")
if cost <= money:
    remainder = money - cost
    remainder = int(remainder)
    print(f"Thank you. Here is your change: \n{remainder}")