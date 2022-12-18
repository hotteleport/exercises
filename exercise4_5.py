# ask user is he a student
yes_no = input("Are you a student? (y/n) \n")
yes_no = yes_no.lower()
price = False
# terms
if yes_no == "n":
    price = False
elif yes_no == "y":
    travel_month = input("Travel month? (1-12) \n")
    travel_month = int(travel_month)
    if travel_month > 12:
        print("Incorrect value")
    elif 6 <= travel_month <= 8:
        price = False
    else:
        price = True
if price:
    print("Special price")
else:
    print("Normal price")
