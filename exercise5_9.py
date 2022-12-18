# make list
name_list = ["Aaron", "Bill", "Mike", "John", "Dylan",
             "James", "Hugo", "Kate", "Lock", "Villy",
             "Sam", "Daniel", "Evangeline", "Lisa", "Max"]

new_list = []
vowels = "AEIOUaeiou"

# make a loop
for name in name_list:
    # depart names to symbols
    letters = [letter for letter in name]
    name_length = len(name)
    # check letters "s" and "e"
    if "s" not in name and "e" not in name:
        # check if  less than 8 letters
        if name_length < 8:
            count = list(map(name.count, "AEIOUaeiou"))
            if sum(count) <= 2:
                new_list.append(name)

# print result
print(new_list)
