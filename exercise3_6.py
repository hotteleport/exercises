# Python program to check if year is a leap year or not
year = input("Give year: \n")
year = int(year)

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("Leap year: YES")

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 == 0) and (year % 100 != 0):
    print("Leap yea: YES")

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("Leap year: NO")