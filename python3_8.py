# ask questions
cost = input("What is your total cost of the order (€)? \n")
cost = float(cost)
student = input("Are you a student? y/n: \n")
vip = input("Are you vip? y/n: \n")
code = input("Do you have a sales code? If yes, write it here: \n")
# if FALL22
# total cost is total cost * 0.1 (10% discount)
if code == "FALL22":
    total_cost = cost - (cost * 0.1)
# elif BK2SCHOOL and user is a student
# total cost is total cost • 0.2 (20% discount)
elif code == "BK2SCHOOL" and student == "y":
    total_cost = cost - (cost * 0.2)
else:
    pass
# calculate vip points
if vip == "y":
    previous_points = input("How many VIP points you have from the previous purchase? \n")
    previous_points = int(previous_points)
    points = cost / 10
    points = round(points, 0)
    new_points = points * 100
    total_points = previous_points + new_points
    reduction = total_points / 1000
    reduction = round(reduction, 0)
    reduction = reduction * 5
    total_cost = cost - reduction
    # print total cost, if cost lower than 99 add 7,95 euro
if total_cost < 99:
        total_cost = total_cost + 7.95
        print(f"You have to pay for shipment. You total cost is {total_cost} euro.")
else:
        print(f"You do not need to pay for shipment. You total cost is {total_cost} euro.")