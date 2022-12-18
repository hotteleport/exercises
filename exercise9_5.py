from functions import *

# ask user a number
number = int(input("Select the operation (1-3), 0 stops the application:\n"))
# conditions
while number == 0:
    print("Thank you for using application!")
    break

if number == 1:
        # values and calculation of the box
        width = int(input("Give box width:\n"))
        height = int(input("Give box height:\n"))
        depth = int(input("Give box depth:\n"))
        formula1 = box_volume(width, height, depth)
        print(f"Box volume: {formula1} m3")
elif number == 2:
        # value and calculation of the ball
        radius = int(input("Give ball radius:\n"))
        formula2 = ball_volume(radius)
        formula2 = round(formula2, 2)
        print(f"Ball volume: {formula2} m3")
elif number == 3:
        # values and calculation of the pipe
        radius2 = int(input("Give pipe radius:\n"))
        length = int(input("Give pipe length:\n"))
        formula3 = pipe_volume(radius2, length)
        formula3 = round(formula3, 2)
        print(f"Pipe volume: {formula3} m3")
