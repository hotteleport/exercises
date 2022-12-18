from functions import *

hours = int(input("Give hours:\n"))
minutes = int(input("Give minutes:\n"))
seconds = int(input("Give seconds:\n"))

result = count_seconds(hours, minutes, seconds)
print(f"{result} seconds in total.")