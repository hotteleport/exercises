import math
# ask user
item = input("Is it a letter or a parcel? Write l or p: \n")
# ask about weight
weight = input("What is a weight of the shipment? \n")
weight = int(weight)
# base cost letter - 50 cents, parcel - 2 euro
if item == "l" and weight <= 200:
    print ("Your shipment cost for letter is 50 cents.")
if item == "p" and weight <= 200:
    print("Your shipment cost for the parcel is 2 euro.")
# conditions
if item == "l" and 200 < weight < 500:
    weight = weight / 100
    weight = math. floor(weight)
    cost = (weight * 4) + 50
    cost = cost / 100
    print(f"Your shipment cost for letter is {cost} euro.")

elif item == "l" and weight > 500:
    mailbox = input ("Does your letter fit the mailbox? y/n: \n")

    if mailbox == "y":
        weight = weight / 100
        weight = math.floor (weight)
        cost = (weight * 7) + 50
        cost = cost / 100
        print(f"Your shipment cost for letter is {cost} euro.")
else:
    weight = weight / 100
    weight = math. floor (weight)
    cost = (weight * 7) + 50 + 200
    cost = cost / 100
    print (f"Your shipment cost for letter is {cost} euro.")

if item == "p" and 200 < weight < 500:
    weight = weight / 100
    weight = math. floor (weight)
    cost = (weight * 8) + 200
    cost = cost / 100
    print(f"Your shipment cost for parcel is {cost} euro.")

elif item == "p" and weight > 500:
    weight = weight / 100
    weight = math. floor (weight)
    cost = (weight * 14) + 200
    cost = cost / 100
    print(f"Your shipment cost for parcel is {cost} euro.")