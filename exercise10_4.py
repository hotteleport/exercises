import json
# open
file = open("countries.json", "r")
data = file.read()
# print data
x = json.loads(data)
print("All countries and capitals:")
# print all needed info
for city in x:
    print(f"{city['country']}: {city['capital']}")
#close
file.close()