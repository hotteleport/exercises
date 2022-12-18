# while statement
"y" == True
while "y":
    # ask radius and calculate S
    radius = int(input("Give radius: "))
    circle_area = 3.14 * (radius * radius)
    print(circle_area)
    continue1 = input("Do you want to continue? (y/n) ")
    # break if no
    if continue1 == "n":
        break





