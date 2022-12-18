# print the list of cities
cities = ["Rome", "Athens", "Stockholm", "London", "Dublin", "Paris"]
c = cities[5]
# sort
cities = sorted(cities)
list.sort(cities)
# result
number = 0
for c in cities:
    number = number + 1
    print(f"{number}: {c}")
