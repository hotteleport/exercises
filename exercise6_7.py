# ask range
range_1 = input("Give the range start: ")
range_1 = int(range_1)
range_2 = input("Give the range end: ")
range_2 = int(range_2)

# create range
range = range(range_1, range_2)

for number in range:
    # / 5 or 7
    if number % 5 == 0 and number % 7 == 0:
        print(f"The number {number} is divisible by both 5 and 7!")
        break
    # / 5
    elif number % 5 != 0:
        print(f"{number} is not divisible by 5, skip")
    # / 7
    elif number % 7 != 0:
        print(f"{number} is not divisible by 7, skip")
# not found
if number % 5 != 0 and number % 7 != 0:
    print("Suitable number is not found in the range!")
