# open file
file = open("artists.txt", "r")
print("Some of the best-selling music albums in history:")
print()
# output info from file
info = file.read()
list_0 = info.split("\n")
for list in list_0:
    print(f"-> {list}")
file.close()

