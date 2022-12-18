total_minutes = input ("How many minuties? ")
total_minutes = int(total_minutes)

hours = total_minutes // 60

minutes = total_minutes % 60

time = "{}h {}min".format(hours, minutes)

print(time)