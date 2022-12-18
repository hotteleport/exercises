import random
# open file
file = open("wisewords.txt", "r")

# output info to list
info = file.read()
list0 = info.split("\n")
# use random
list0 = random.choice(list0)
# result
print("Today's proverb:")
print(list0)
#close
file.close()