# use tuple
months = tuple(["January", "February", "March", "April", "May", "June", "Jule", "August", "September","October", "November", "December"])
# choose number of the month
choice = input("Give the number of month: ")
# subtract 1, because months starts from 0
choice = int(choice) - 1
print(months[choice])
