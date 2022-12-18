# ask questions
cost = input("What is your total cost of the order €? \n")
cost = float (cost)
student = input("Are you a student? y/n: \n")
vip = input ("Are you vip? y/n: \n")
code = input ("Do you have a sales code? If yes, write it here: \n")
# FALL22 = 10% discount
if code == "FALL22":
    total_cost = cost - (cost * 0.1)
# BK2SCHOOL = 20%
elif code == "BK2SCHOOL" and student == "y":
    total_cost = cost - (cost * 0.2)
else:
    pass
# calculate vip points
if vip == "y":
    last_points = input("How many vip points you have from the last purchase? \n")
    last_points = int(last_points)
    points = cost / 10
    points = round(points, 0)
    new_points = points * 100
    total_points = last_points + new_points
    reduction = total_points / 1000
    reduction = round(reduction, 0)
    reduction = reduction * 5
    total_cost = cost - reduction
    # total cost
if total_cost < 99:
        total_cost = total_cost + 7.95
        print(f"You have to pay for delivery. You total cost is {total_cost} euro.")
else:
        print(f"You do not need to pay for delivery. You total cost is {total_cost} euro.")