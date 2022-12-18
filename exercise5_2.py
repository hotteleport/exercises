# I use "for loop"
total = 0
for x in range(12):
    # ask user 12 times rain amount of month
    number = int(input("Give rain amount of month: "))
    total = total + number
    # calculate average of month
    average = total / 12
    print(f"Year average for rain = {average} mm")